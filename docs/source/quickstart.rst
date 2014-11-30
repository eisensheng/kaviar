.. -*- encoding: utf-8 -*-
.. _quickstart:


Quickstart
==========

Eager to get started?  Good!  This page consists only of examples to give you
an introduction in how you can make effective use of Kaviar in your project.


Formatting
----------

.. module:: kaviar

>>> from kaviar import kv_format

.. testsetup:: *

    from kaviar import kv_format

.. doctest::

    >>> kv_format(random_value=4)  # chosen by fair dice roll.
    >>>                            # guaranteed to be random.
    'random_value=4'


Strings and Binary Data
~~~~~~~~~~~~~~~~~~~~~~~

.. doctest::

    >>> kv_format(simple_string='Hi!')
    'simple_string=Hi!'

.. doctest::

    >>> kv_format(complex_string='Hello World!')
    'complex_string="Hello World!"'

.. doctest::

    >>> print(kv_format(unicode_string='こにちは'))
    unicode_string="\u3053\u306b\u3061\u306f"

.. doctest::

    >>> print(kv_format(data=b'\xbc\xe1#R\n\xa0\x08D\xe5'))
    data="\xbc\xe1#R\n\xa0\bD\xe5"


Lists, Sets and anything that can be iterated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doctest::

    >>> kv_format(a=[1, 2, 3, ])
    'a__0=1   a__1=2   a__2=3'

.. doctest::

    >>> kv_format(my_set={'z', 'x', 'y'})
    'my_set__0=x   my_set__1=y   my_set__2=z'


Mappings
~~~~~~~~

.. doctest::

    >>> kv_format(c={'b': 16, 'a': 27, })
    'c__a=27   c__b=16'


.. doctest::

    >>> from collections import OrderedDict
    >>> kv_format(o=OrderedDict([('b', 16), ('a', 27), ]))
    'o__b=16   o__a=27'


Other Objects
~~~~~~~~~~~~~

.. doctest::

    >>> import datetime
    >>> kv_format(t=datetime.datetime(2014, 12, 24, 12, 12))
    't="2014-12-24 12:12:00"'


.. doctest::

    >>> from decimal import Decimal
    >>> kv_format(c=Decimal('0.24'))
    'c=0.24'


Logging
-------

Simple logging
~~~~~~~~~~~~~~

.. testcode::

    from kaviar import EventKvLoggerAdapter

    logger = EventKvLoggerAdapter.get_logger(__name__)

    logger.info('NEW_CLIENT', client_id=42,
                peer_name='93.184.216.119')


Predefined Event logging
~~~~~~~~~~~~~~~~~~~~~~~~

.. testcode::

    import logging
    from functools import partial
    from kaviar import EventKvLoggerAdapter

    logger = EventKvLoggerAdapter.get_logger(__name__)

    log_event = partial(logger.define_logger_func(logging.INFO,
                                                  'server peer_name'),
                        'NEW_CLIENT')

    log_event('example.org', '93.184.216.164')
