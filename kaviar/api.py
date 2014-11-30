# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from collections import Mapping, Iterable
from inspect import isroutine
from itertools import chain

from .dumping import dump_dict, dump_key_values


DEFAULT_SEPARATOR = '   '


def _format_pairs(kv_pairs, separator=DEFAULT_SEPARATOR):
    return separator.join('{0!s}={1!s}'.format(x, y) for x, y in kv_pairs)


def kv_format_dict(d, keys=None, separator=DEFAULT_SEPARATOR):
    """Formats the given dictionary ``d``.

    For more details see :func:`kv_format`.

    :param collections.Mapping d:
        Dictionary containing values to format.
    :param collections.Iterable keys:
        List of keys to extract from the dict.
    :param str separator:
        Value between two pairs.
    :return:
        Key-Value formatted content generated from ``d``.
    :rtype:
        :data:`six.text_type <six:six.text_type>`
    """
    return _format_pairs(dump_dict(d, keys), separator=separator)


def kv_format_pairs(pairs, separator=DEFAULT_SEPARATOR):
    """Formats the given Key-Value pairs in ``kv_pairs``.

    For more details see :func:`kv_format`.

    :param collections.Iterable kv_pairs:
        List of Key-Value pairs to format.
    :param str separator:
        Value between two pairs.
    :return:
        Key-Value formatted content generated from ``kv_pairs``.
    :rtype:
        :data:`six.text_type <six:six.text_type>`
    """
    return _format_pairs(dump_key_values(pairs), separator)


def kv_format_object(o, keys=None, separator=DEFAULT_SEPARATOR):
    """Formats an object's attributes.  Useful for object representation
    implementation.  Will skip methods or private attributes.

    For more details see :func:`kv_format`.

    :param o:
        Object to format.
    :param collections.Sequence keys:
        Explicit list of attributes to format.  ``None`` means all public
        visible attribute for the given object will be formatted.
    :param str separator:
        Value between two pairs.
    :return:
        Formatted Object attributes.
    :rtype:
        :data:`six.text_type <six:six.text_type>`
    """
    if keys is None:
        key_values = []
        for k, v in ((x, getattr(o, x)) for x in sorted(dir(o))):
            if k.startswith('_') or isroutine(v):
                continue
            key_values += (k, v),
    else:
        key_values = ((k, getattr(o, k)) for k in keys)

    return kv_format_pairs(key_values, separator)


def kv_format(*args, **kwargs):
    """Formats any given list of Key-Value pairs or dictionaries in ``*args``
    and any given keyword argument in ``**kwargs``.

    Any item within a given list or dictionary will also be visited and
    added to the output.  Strings will be escaped to prevent leaking binary
    data, ambiguous characters or other control sequences.  Strings with
    escaped characters or spaces  will be encapsulated in quotes.
    Other objects will be converted into a string and will be treated
    as a string afterwards.

    :param \*args:
        Values to format.
    :type \*args:
        any Iterable or Mapping
    :param \*\*kwargs:
        Keyword Values to format
    :return:
        Formatted content of ``*args`` and ``**kwargs``.
    :rtype:
        :data:`six.text_type <six:six.text_type>`
    """
    pairs = ((dump_dict(arg) if isinstance(arg, Mapping)
              else (dump_key_values(arg) if isinstance(arg, Iterable)
                    else None))
             for arg in args + (kwargs, ))
    return _format_pairs(chain.from_iterable(p for p in pairs if p))
