# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from collections import namedtuple

from six import text_type

from kaviar import kv_format, kv_format_dict, kv_format_pairs, kv_format_object


def test_return_type_text():
    assert isinstance(kv_format(a='HalloWelt!'), text_type)


def test_format_dict():
    assert kv_format_dict({'a': 42, }) == 'a=42'


def test_format_dict_keys():
    assert kv_format_dict({'a': 42, 'b': 27, 'c': 23, },
                          ['a', 'b', ]) == 'a=42   b=27'


def test_format_pairs():
    assert kv_format_pairs([('a', 96), ]) == 'a=96'


def test_format_object():
    assert (kv_format_object(namedtuple('NamedTuple', 'a b c')(3, 6, 9))
            == 'a=3   b=6   c=9')
