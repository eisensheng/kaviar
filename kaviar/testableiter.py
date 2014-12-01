# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from six import next


class TestableIter(object):

    def __init__(self, it):
        self.iter, self.stack = it, []

    def __iter__(self):
        return self

    def __bool__(self):
        try:
            self.stack += next(self.iter),
        except StopIteration:
            return len(self.stack) > 0
        else:
            return True

    __nonzero__ = __bool__

    def __next__(self):
        try:
            return self.stack.pop(0)
        except IndexError:
            return next(self.iter)

    next = __next__
