# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import pytest
from kaviar import kv_format_object


@pytest.fixture
def fake_object():
    class FakeObject(object):
        class_attr = 42

        def __init__(self):
            self._protected_attribute = 'protected'
            self.__private_attribute = 'privates'
            self.obj_attr = 23
            self.another_attr = 29

        def a(self):  # pragma: no cover
            pass

        def b(self):  # pragma: no cover
            pass

    return FakeObject()


def test_format_object_keyless(fake_object):
    assert (kv_format_object(fake_object)
            == 'another_attr=29   class_attr=42   obj_attr=23')


def test_format_object_keys(fake_object):
    assert (kv_format_object(fake_object, ['another_attr', 'class_attr', ])
            == 'another_attr=29   class_attr=42')
