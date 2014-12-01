# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import pytest

from kaviar import KvFormatter, ListFilter
from tests.conftest import skip_if_pypy


@skip_if_pypy
def test_simple_format():
    formatter = KvFormatter('a b c')
    assert formatter(3, 6, 9) == 'a=3   b=6   c=9'


@skip_if_pypy
def test_preserve_ordering():
    formatter = KvFormatter('z y x')
    assert formatter(3, 6, x=9) == 'z=3   y=6   x=9'


@skip_if_pypy
def test_default_value():
    formatter = KvFormatter(['a', 'b', ('c', 'default')])

    assert formatter(3, 6) == 'a=3   b=6   c=default'
    assert formatter(3, 6, c=9) == 'a=3   b=6   c=9'


@skip_if_pypy
def test_filter():
    formatter = KvFormatter(['a', 'b', ], filters={'b': ListFilter, })
    assert formatter(3, [6, 9, 12]) == 'a=3   b=6,9,12'


@skip_if_pypy
def test_filter_fuzzy_feed():
    with pytest.raises(TypeError) as exc_info:
        KvFormatter(['a', 'b', ], filters={'c': ListFilter, })

    assert ("extra filter for unexpected filter 'c'", ) == exc_info.value.args
