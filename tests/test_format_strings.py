# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from kaviar import kv_format


def test_lower_unicode_signs():
    assert (kv_format(a=('\x00\x01\x02\x03\x04\x05\x06\x07'
                         '\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
                         '\x10\x11\x12\x13\x14\x15\x16\x17'
                         '\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'))
            == ('a="\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\b'
                '\\t\\n\\x0b\\f\\r\\x0e\\x0f\\x10\\x11\\x12\\x13'
                '\\x14\\x15\\x16\\x17\\x18\\x19\\x1a\\x1b\\x1c'
                '\\x1d\\x1e\\x1f"'))


def test_c1_escape():
    assert kv_format(a='Hallo\u00a0Welt!') == 'a="Hallo\\xa0Welt!"'


def test_c1_not_escape_upper_limit():
    assert kv_format(a='H\u00a1') == 'a=H\u00a1'


def test_c1_not_escape_lower_limit():
    assert kv_format(a='Hi~') == 'a=Hi~'


def test_unescaped():
    assert kv_format(a='HalloWelt!') == 'a=HalloWelt!'


def test_string_quoted():
    assert kv_format(a='Hallo "Welt"!') == 'a="Hallo \\"Welt\\"!"'


def test_random_bytes():
    assert (kv_format(c=b'\nJxd\x88\xfaJx;\x116\xe6')
            == 'c="\\nJxd\\x88\\xfaJx;\\x116\\xe6"')


def test_unicode_text_latin1():
    assert kv_format(g='Wörk Wörk') == 'g="Wörk Wörk"'


def test_unicode_text_non_latin1():
    assert kv_format(g='こにちは') == 'g="\\u3053\\u306b\\u3061\\u306f"'


def test_supplementary_unicode():
    assert kv_format(f='\U00010392') == 'f="\\U00010392"'
