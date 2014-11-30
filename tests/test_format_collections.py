# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import pytest

from kaviar import kv_format
from kaviar.auxiliary import OrderedDict


def test_simple_dict():
    assert (kv_format(a={'x': 1, 'y': 2, 'z': 3, })
            == 'a__x=1   a__y=2   a__z=3')


def test_simple_list():
    assert kv_format(l=[6, 2]) == 'l__0=6   l__1=2'


def test_simple_set():
    assert kv_format(a=set(['a', 'b', ])) == 'a__0=a   a__1=b'


def test_empty_list():
    assert kv_format(h=[]) == 'h=EMPTY'


def test_empty_dict():
    assert kv_format(j={}) == 'j=EMPTY'


def test_empty_set():
    assert kv_format(n=set()) == 'n=EMPTY'


def test_empty_dict_and_list_in_list():
    assert kv_format(i=[{}, []]) == 'i__0=EMPTY   i__1=EMPTY'


def test_nested_list():
    assert (kv_format(l=[['Nested', 'List'],
                         {'a': 23, 'b': 42, }, ],
                      d={'x': 'Test', 'y': 'String', })
            == ('d__x=Test   d__y=String'
                '   l__0__0=Nested   l__0__1=List'
                '   l__1__a=23   l__1__b=42'))


def test_nested_dict():
    assert (kv_format(v={'z': [1, 2, 3],
                         'y': {'c': 27, 'b': 36, 'a': 96, },
                         'x': [{'u': 27, 'v': 42},
                               {'v': 46, 'u': 49, }, ], })
            == ('v__x__0__u=27   v__x__0__v=42   v__x__1__u=49'
                '   v__x__1__v=46   v__y__a=96   v__y__b=36'
                '   v__y__c=27   v__z__0=1   v__z__1=2   v__z__2=3'))


@pytest.mark.skipif(OrderedDict is None,
                    reason='OrderedDict unavailable')
def test_ordered_dict():
    ordered_dict = OrderedDict([('z', 26), ('y', 25), ('x', 24), ('w', 23),
                                ('v', 22), ('u', 21), ('t', 20), ])
    assert (kv_format(ordered_dict)
            == 'z=26   y=25   x=24   w=23   v=22   u=21   t=20')
