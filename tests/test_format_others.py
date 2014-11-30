# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from datetime import datetime
from decimal import Decimal

from kaviar import kv_format


def test_decimal():
    assert kv_format(delta=Decimal('4.50')) == 'delta=4.50'


def test_datetime():
    assert (kv_format(date=datetime(2013, 9, 23, 11, 11, 11))
            == 'date="2013-09-23 11:11:11"')


def test_boolean():
    assert kv_format(success=True, fail=False) == 'fail=False   success=True'
