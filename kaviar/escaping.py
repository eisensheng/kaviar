# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function,
                        unicode_literals, division)

from six import int2byte, iterbytes, text_type


ESCAPE_MAP = {ord('\\'): '\\\\', ord('"'): '\\"', ord('\b'): '\\b',
              ord('\f'): '\\f', ord('\n'): '\\n', ord('\r'): '\\r',
              ord('\t'): '\\t', }

DEFAULT_MAX_CODE_POINT = 0xff
DEFAULT_QUOTE_ON = ' \\'
QUOTE_ALWAYS = object()


def _quote_filter(value, quote_on=DEFAULT_QUOTE_ON):
    if quote_on is QUOTE_ALWAYS or next((True for x in value
                                         if x in quote_on), False):
        value = '"{0}"'.format(value)
    return value


def escape_text(text, quotes_on=DEFAULT_QUOTE_ON,
                max_code_point=DEFAULT_MAX_CODE_POINT):
    out = []
    for n, t in ((ord(x), x) for x in text):
        try:
            t = ESCAPE_MAP[n]
        except KeyError:
            if n < 0x20 or 0xA0 >= n >= 0x7f or n > max_code_point:
                t = '\\' + ('x{0:02x}' if n < 0x100
                            else ('u{0:04x}' if n < 0x10000
                                  else 'U{0:08x}')).format(n)
        out += t,
    return _quote_filter(''.join(out), quotes_on)


def escape_bytes(s, quotes_on=DEFAULT_QUOTE_ON):
    out = (b''.join(int2byte(x) if 0x7f > x > 0x1f
                    else (ESCAPE_MAP.get(x, (r'\x{0:02x}'.format(x)))
                          .encode('ascii'))
                    for x in iterbytes(s))).decode('ascii')
    return _quote_filter(out, quotes_on)


def escape_arbitrary_bytes(s, quotes_on=DEFAULT_QUOTE_ON,
                           max_code_point=DEFAULT_MAX_CODE_POINT):
    return (escape_text(s, quotes_on, max_code_point)
            if isinstance(s, text_type) else escape_bytes(s, quotes_on))
