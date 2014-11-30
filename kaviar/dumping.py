# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function,
                        unicode_literals, division)

from inspect import isgenerator
from collections import Mapping, Iterable
from six import text_type, binary_type

from .auxiliary import OrderedDict
from .escaping import escape_arbitrary_bytes
from .filterbase import FilterBase
from .testableiter import TestableIter


def dump_dict(d, keys=None):
    if keys is None:
        keys = (d.keys() if OrderedDict and isinstance(d, OrderedDict)
                else sorted(d.keys()))
    return dump_key_values((k, d[k]) for k in keys)


def dump_list(l):
    if not hasattr(l, '__getitem__'):
        # assume objects without __getitem__ don't enforce an ordering
        l = sorted(l)
    return dump_key_values((text_type(i), v) for i, v in enumerate(l))


def dump_generator(k, g):
    g = TestableIter(g)
    if g:
        for k_, v_ in g:
            yield '{0!s}__{1}'.format(k, k_), v_
    else:
        yield k, 'EMPTY'


def dump_key_values(kv_iterable):
    for k, v in kv_iterable:
        k = escape_arbitrary_bytes(k)
        if isinstance(v, FilterBase):
            v = v.to_value()
            if isgenerator(v):
                for k_, v_ in dump_generator(k, v):
                    yield k_, v_
            else:
                yield k, v
        elif isinstance(v, (text_type, binary_type)):
            yield k, escape_arbitrary_bytes(v)
        elif isinstance(v, Iterable):
            g = dump_generator(k, (dump_dict(v) if isinstance(v, Mapping)
                                   else dump_list(v)))
            for k_, v_ in g:
                yield k_, v_
        else:
            yield k, escape_arbitrary_bytes(text_type(v))
