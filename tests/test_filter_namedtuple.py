# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from collections import namedtuple as py_namedtuple

from namedlist import namedtuple as nl_namedtuple, namedlist as nl_namedlist

from kaviar import kv_format, NamedTupleFilter
from .conftest import skip_if_pypy


def test_python_tuple():
    n_tuple = py_namedtuple('TestTuple', 'a b')

    assert (kv_format(f=NamedTupleFilter(n_tuple(24, 23)))
            == 'f__a=24   f__b=23')


@skip_if_pypy
def test_named_list_tuple():
    n_tuple = nl_namedtuple('TestTuple', 'a b')
    assert (kv_format(f=NamedTupleFilter(n_tuple(24, 23)))
            == 'f__a=24   f__b=23')


@skip_if_pypy
def test_named_list():
    n_list = nl_namedlist('NamedList', 'a b')
    assert (kv_format(f=NamedTupleFilter(n_list(24, 23)))
            == 'f__a=24   f__b=23')
