# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import sys

import pytest


skip_if_pypy = pytest.mark.skipif('__pypy__' in sys.builtin_module_names,
                                  reason='feature disabled in pypy')
