# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function,
                        unicode_literals, division)

from six import text_type, binary_type

from .escaping import (escape_arbitrary_bytes, QUOTE_ALWAYS,
                       DEFAULT_QUOTE_ON, DEFAULT_MAX_CODE_POINT)
from .filterbase import FilterBase, QuotedFilterBase
from .dumping import dump_key_values


UNLIMITED_LENGTH = object()


class TextFilter(QuotedFilterBase):
    """Provides a filtering facility to specify how a string will be seen in
    a Key-Value formatted line.

    :param value:
        Value to log. Can be anything from a string to an object
        which implements ``object.__str__``.
    :param str quotes_on:
        Put output in parentheses if output contains
        any of the given arguments.
    :param bool plaintext:
        Don't escape characters beyond Basic Latin and Latin-1 Unicode block.
    :param int max_length:
        Truncate values beyond given value.  Truncated values will be
        explicitly marked.
    """

    def __init__(self, value, quotes_on=DEFAULT_QUOTE_ON, plaintext=False,
                 max_length=UNLIMITED_LENGTH):
        super(TextFilter, self).__init__(value, quotes_on)
        self.plaintext, self.max_length = plaintext, max_length

    def to_value(self):
        v = (self.value if isinstance(self.value, (text_type, binary_type))
             else text_type(self.value))

        v, t = ((v, False) if self.max_length is UNLIMITED_LENGTH
                else (v[:self.max_length], len(v) > self.max_length))

        return (escape_arbitrary_bytes(v,
                                       QUOTE_ALWAYS if t else self.quotes_on,
                                       (2 ** 32 - 1 if self.plaintext
                                        else DEFAULT_MAX_CODE_POINT)) +
                ('' if not t else '[T]'))


class ListFilter(QuotedFilterBase):
    """Allows to embed iterable values in a comma separated format instead of
    the default format.

    :param abc.Iterable value:
        Anything that can be iterated. Items will be converted to string if
        necessary.  Also supports :class:`TextFilter` instances.
    """

    def to_value(self):
        quote_on = (self.quotes_on if self.quotes_on is QUOTE_ALWAYS
                    else DEFAULT_QUOTE_ON + ',')
        return ','.join((x if isinstance(x, TextFilter)
                         else TextFilter(x, quote_on)).to_value()
                        for x in self.value)


class NamedTupleFilter(FilterBase):
    """Dump :func:`namedtuple` based instances in a key-value format where
    the corresponding name for a field will be used instead of the index.
    The Order of fields will be preserved.

    :param value:
        :func:`namedtuple` or :func:`namedlist` based instances.  Or anything
        else that can be iterated and has a ``_fields`` attribute.
    """

    def to_value(self):
        return dump_key_values(zip(self.value._fields, self.value))
