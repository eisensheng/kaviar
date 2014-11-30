# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import pytest

from kaviar import kv_format, TextFilter, QUOTE_ALWAYS


def test_escape_non_latin():
    assert (kv_format(g=TextFilter('こにちは'))
            == 'g="\\u3053\\u306b\\u3061\\u306f"')


def test_escape_non_latin_length_limited():
    assert (kv_format(g=TextFilter('こにちは', max_length=3))
            == 'g="\\u3053\\u306b\\u3061"[T]')


def test_plain_text():
    assert (kv_format(g=TextFilter('こにちは', plaintext=True)
            == 'g=こにちは'))


def test_plain_text_length_limited():
    assert (kv_format(g=TextFilter('こにちは', plaintext=True, max_length=3))
            == 'g="こにち"[T]')


def test_plain_text_length_limited_force_quote():
    assert (kv_format(g=TextFilter('こにちは',
                                   plaintext=True,
                                   quotes_on=QUOTE_ALWAYS,
                                   max_length=3))
            == 'g="こにち"[T]')


def test_plain_text_quoted():
    assert kv_format(g=TextFilter('こにちは', plaintext=True,
                                  quotes_on=QUOTE_ALWAYS)) == 'g="こにちは"'


def test_integer_input():
    assert kv_format(g=TextFilter(42)) == 'g=42'


@pytest.mark.parametrize('value', [b'HalloWelt', 'HalloWelt'])
class TestTextDataAgnostic:

    def test_max_length_below(self, value):
        assert kv_format(f=TextFilter(value, max_length=4)) == 'f="Hall"[T]'

    def test_max_length_equal(self, value):
        assert kv_format(f=TextFilter(value, max_length=9)) == 'f=HalloWelt'

    def test_max_length_above(self, value):
        assert kv_format(f=TextFilter(value, max_length=255)) == 'f=HalloWelt'

    def test_force_quotes(self, value):
        assert kv_format(f=TextFilter(value, QUOTE_ALWAYS)) == 'f="HalloWelt"'
