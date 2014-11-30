# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import abc

from six import with_metaclass

from .escaping import DEFAULT_QUOTE_ON


class FilterBase(with_metaclass(abc.ABCMeta)):

    def __init__(self, value, quotes_on=DEFAULT_QUOTE_ON):
        self.value, self.quotes_on = value, quotes_on

    @abc.abstractmethod
    def to_value(self):
        pass  # pragma: no cover  # it's just a abstractmethod stub, c'mon!


class QuotedFilterBase(with_metaclass(abc.ABCMeta, FilterBase)):

    def __init__(self, value, quotes_on=DEFAULT_QUOTE_ON):
        super(QuotedFilterBase, self).__init__(value)
        self.quotes_on = quotes_on
