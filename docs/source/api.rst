.. -*- encoding: utf-8 -*-
.. _api:


API
===

All public visible symbols can be directly imported from the ``kaviar``
module.  This is also the preferred method to use Kaviar.


Formatting Functions
--------------------

.. module:: kaviar

.. autofunction:: kv_format_pairs
.. autofunction:: kv_format_dict
.. autofunction:: kv_format_object
.. autofunction:: kv_format


Logging Adapters
----------------

.. autoclass:: KvLoggerAdapter
    :members:
    :exclude-members: define_logger_func

    .. automethod:: define_logger_func(self, level, field_names, default=NO_DEFAULT, filters=None, include_exc_info=False)

.. autoclass:: PositionalArgsAdapter

    .. autoattribute:: positional_args

.. autoclass:: EventKvLoggerAdapter


Filtering
---------

.. autoclass:: TextFilter(value, quotes_on=DEFAULT_QUOTE_ON, plaintext=False, max_length=UNLIMITED_LENGTH)

.. autoclass:: ListFilter(value, quotes_on=DEFAULT_QUOTE_ON, plaintext=False, max_length=UNLIMITED_LENGTH)

.. autoclass:: NamedTupleFilter(value, quotes_on=DEFAULT_QUOTE_ON, plaintext=False, max_length=UNLIMITED_LENGTH)


Function Tools
--------------

.. autoclass:: KvFormatter(self, field_names, default=namedlist.NO_DEFAULT, filters=None)
