# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function,
                        unicode_literals, division)

from .adapter import (KvLoggerAdapter, PositionalArgsAdapter,
                      EventKvLoggerAdapter)
from .escaping import QUOTE_ALWAYS, DEFAULT_QUOTE_ON, DEFAULT_MAX_CODE_POINT
from .filters import TextFilter, ListFilter, NamedTupleFilter
from .api import kv_format_dict, kv_format_pairs, kv_format_object, kv_format
from .functools import KvFormatter


__version__ = '1.0'

__all__ = ['KvLoggerAdapter', 'PositionalArgsAdapter',
           'EventKvLoggerAdapter',

           'kv_format_pairs', 'kv_format_dict', 'kv_format_object',
           'kv_format',

           'QUOTE_ALWAYS', 'DEFAULT_QUOTE_ON', 'DEFAULT_MAX_CODE_POINT',

           'KvFormatter',

           'TextFilter', 'ListFilter', 'NamedTupleFilter', ]
