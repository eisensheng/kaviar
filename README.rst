.. -*- coding: utf-8 -*-

Kaviar
======

.. image:: https://img.shields.io/travis/eisensheng/kaviar.svg?style=flat
    :target: https://travis-ci.org/eisensheng/kaviar
    :alt: Continuous Integration

.. image:: https://img.shields.io/coveralls/eisensheng/kaviar/develop.svg?style=flat
    :target: https://coveralls.io/r/eisensheng/kaviar?branch=develop
    :alt: Test Coverage

.. image:: https://readthedocs.org/projects/kaviar/badge/?version=latest&style=flat
    :target: http://kaviar.readthedocs.org/en/latest/
    :alt: Documentation

.. image:: https://pypip.in/version/kaviar/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/kaviar/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/kaviar/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/kaviar/
    :alt: Python versions

.. image:: https://pypip.in/license/kaviar/badge.svg?style=flat
    :target: https://github.com/eisensheng/kaviar/blob/develop/COPYING
    :alt: MIT License


Simplified event and data formatting and logging.

Kaviar aids developers in need of a convenient way to produce structured
representation of key-value pairs for logging or representation with a 
fixed human and machine friendly syntax suited for later evaluation or
just aesthetic reasons.


Example
-------

Logging a certain event:

.. code-block:: python

    import logging
    from kaviar import EventKvLoggerAdapter
    
    logging.basicConfig(level=logging.DEBUG)
    logger = EventKvLoggerAdapter.get_logger(__name__)
    logger.info('NEW_CLIENT', client_id=42, peer_name='93.184.216.119')


Separating the event definition from actual logging:

.. code-block:: python

    import logging
    from functools import partial
    from kaviar import EventKvLoggerAdapter
    
    logging.basicConfig(level=logging.DEBUG)
    logger = EventKvLoggerAdapter.get_logger(__name__)
    
    log_event = partial(logger.define_logger_func(logging.INFO,
                                                  'server peer_name'),
                        'NEW_CLIENT')
    
    log_event('example.org', '93.184.216.164')

