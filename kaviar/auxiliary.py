# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

try:
    from collections import OrderedDict
except ImportError:
    try:
        from ordereddict import OrderedDict
    except ImportError:
        OrderedDict = None
