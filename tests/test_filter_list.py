# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from kaviar import kv_format, ListFilter, QUOTE_ALWAYS, TextFilter


def test_integers():
    assert kv_format(f=ListFilter([1, 2, 3])) == 'f=1,2,3'


def test_text():
    assert kv_format(f=ListFilter(['a', 'b', 'c', ])) == 'f=a,b,c'


def test_comma_in_text():
    list_filter = ListFilter(['a', 'b, c', 'd', ])
    assert kv_format(f=list_filter) == 'f=a,"b, c",d'


def test_force_quotes():
    list_filter = ListFilter(['a', 'b', 'c', ], quotes_on=QUOTE_ALWAYS)
    assert kv_format(f=list_filter) == 'f="a","b","c"'


def test_escaping():
    list_filter = ListFilter(['a"b', 'c', 'd', ])
    assert kv_format(f=list_filter) == 'f="a\\\"b",c,d'


def test_escaping_non_latin():
    list_filter = ListFilter(['a', 'こにちは', 'd', ])
    assert kv_format(f=list_filter) == 'f=a,"\\u3053\\u306b\\u3061\\u306f",d'


def test_text_filter():
    list_filter = ListFilter([1, TextFilter('こにちは', QUOTE_ALWAYS,
                                            plaintext=True), 2])
    assert kv_format(f=list_filter) == 'f=1,"こにちは",2'
