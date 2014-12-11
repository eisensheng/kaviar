# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function,
                        unicode_literals, division)
from itertools import chain

from logging import (getLogger, LoggerAdapter,
                     DEBUG, INFO, WARNING, ERROR, CRITICAL)

from six.moves import zip

from .api import kv_format
from .functools import KvFormatter, NO_DEFAULT


def _normalize_name(chunks):
    if not chunks:
        return None

    particles = chain.from_iterable(x.split('.') for x in chunks
                                    if hasattr(x, 'split'))
    return '.'.join(x for x in (y.strip() for y in particles) if x)


class KvLoggerAdapter(LoggerAdapter):
    """Simple Adapter for loggers to produce Key-Value structured log messages.

    :param logging.Logger logger:
        the logger to encapsulate.
    :param collections.Mapping extra:
        additional information to log with each message.
    """

    def __init__(self, logger, extra=None):
        if extra is None:
            extra = {}
        try:
            super(KvLoggerAdapter, self).__init__(logger, extra)
        except TypeError:  # py26 incompatibility *sigh*
            LoggerAdapter.__init__(self, logger, extra)

    def _get_kwargs(self, args, kwargs):
        return dict(self.extra, **kwargs)

    def _format(self, args, kwargs):
        return kv_format(self._get_kwargs(args, kwargs))

    def _log(self, level, value, exc_info=False):
        return self.logger.log(level, '%s', value, exc_info=exc_info)

    def _log_kw(self, level, args, kwargs, exc_info=False):
        return self._log(level, self._format(list(args), kwargs), exc_info)

    @classmethod
    def get_logger(cls, *name, **kwargs):
        """Construct a new :class:`KvLoggerAdapter` which encapsulates
        the :class:`logging.Logger` specified by ``name``.

        :param name:
            Any amount of symbols.  Will be concatenated and normalized
            to form the logger name.  Can also be empty.
        :param extra:
            Additional context relevant information.
        :return:
            A new :class:`KvLoggerAdapter` instance ready to use.
        :rtype:
            :class:`KvLoggerAdapter`
        """
        return cls(getLogger(_normalize_name(name)),
                   kwargs.get('extra', None))

    def define_logger_func(self, level, field_names, default=NO_DEFAULT,
                           filters=None, include_exc_info=False):
        """Define a new logger function that will log the given arguments
        with the given predefined keys.

        :param level:
            The log level to use for each call.
        :param field_names:
            Set of predefined keys.
        :param default:
            A default value for each key.
        :param filters:
            Additional filters for treating given arguments.
        :param include_exc_info:
            Include a stack trace with the log.  Useful for the ``ERROR``
            log level.
        :return:
            A function that will log given values with the predefined
            keys and the given log level.
        """
        kv_formatter = KvFormatter(field_names, default, filters)
        return lambda *a, **kw: self._log(level, kv_formatter(*a, **kw),
                                          include_exc_info)

    def log(self, level, *args, **kwargs):
        """Delegate a log call to the underlying logger."""
        return self._log_kw(level, args, kwargs)

    def debug(self, *args, **kwargs):
        """Delegate a debug call to the underlying logger."""
        return self._log_kw(DEBUG, args, kwargs)

    def info(self, *args, **kwargs):
        """Delegate a info call to the underlying logger."""
        return self._log_kw(INFO, args, kwargs)

    def warning(self, *args, **kwargs):
        """Delegate a warning call to the underlying logger."""
        return self._log_kw(WARNING, args, kwargs)

    def error(self, *args, **kwargs):
        """Delegate a error call to the underlying logger."""
        return self._log_kw(ERROR, args, kwargs)

    def exception(self, *args, **kwargs):
        """Delegate a exception call to the underlying logger."""
        return self._log_kw(ERROR, args, kwargs, exc_info=True)

    def critical(self, *args, **kwargs):
        """Delegate a critical call to the underlying logger."""
        return self._log_kw(CRITICAL, args, kwargs)


class PositionalArgsAdapter(KvLoggerAdapter):
    """Adapter for loggers similar to :class:`KvLoggerAdapter` with
    support for positional arguments for predefined keys.
    """

    #: List of predefined keys. The order will be preserved when formatting.
    positional_args = []

    def _format(self, args, kwargs, kv_formatter_pairs=None):
        args_ = tuple(zip(self.positional_args, args))
        if len(args_) < len(self.positional_args):
            raise TypeError(("missing required positional argument: '{0}'"
                             .format(self.positional_args[len(args_)])))

        kv_args_ = ([args_, ] if kv_formatter_pairs is None
                    else [args_, kv_formatter_pairs, ])
        kv_args_ += self._get_kwargs(args[len(args_):], kwargs),
        return kv_format(*kv_args_)

    def define_logger_func(self, level, field_names, default=NO_DEFAULT,
                           filters=None, include_exc_info=False):
        kv_formatter = KvFormatter(field_names, default, filters)

        def __logger_func(*args, **kwargs):
            pairs = kv_formatter.pairs(*args[len(self.positional_args):],
                                       **kwargs)
            return self._log(level, self._format(args, kwargs, pairs),
                             include_exc_info)

        return __logger_func


class EventKvLoggerAdapter(PositionalArgsAdapter):
    """Adapter for loggers which will always have the event key in front of
    each message for easing differentiating between different log events.
    """
    positional_args = ['event', ]
