# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function,
                        unicode_literals, division)
from itertools import chain

from namedlist import namedtuple, NO_DEFAULT
from six import iteritems, iterkeys

from .api import kv_format_pairs


def _validate_filters(fields, filters):
    for field in iterkeys(filters):
        if field in fields:
            continue
        raise TypeError(("extra filter for unexpected filter '{0}'"
                         .format(field)))
    return filters.copy()


class KvFormatter(object):
    """Predefine a list of fields with optional default values and filters.
    The resulting object allows to reuse the field names for formatting
    purpose when called.
    """

    def __init__(self, field_names, default=NO_DEFAULT, filters=None):
        self.args_tuple = namedtuple('_ArgsTuple', field_names, default)
        self.fields = self.args_tuple._fields
        self.filters = (_validate_filters(self.fields, filters)
                        if filters else {})

    def pairs(self, *args, **kwargs):
        items = dict((k, self.filters.get(k, lambda a: a)(v))
                     for k, v in chain(zip(self.fields, args),
                                       iteritems(kwargs)))
        return zip(self.fields, self.args_tuple(**items))

    def __call__(self, *args, **kwargs):
        return kv_format_pairs(self.pairs(*args, **kwargs))
