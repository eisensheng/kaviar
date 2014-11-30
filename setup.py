#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages


def _get_version():
    with io.open('kaviar/__init__.py', encoding='utf-8') as f:
        return re.search("__version__\s*=\s*'([^']+)'\s*", f.read()).group(1)


def _read_long_description():
    with io.open('README.rst', encoding='utf-8') as ld_stream:
        return ld_stream.read()


setup(name='kaviar',
      version=_get_version(),
      description='Simplified event and data formatting and logging.',
      long_description=_read_long_description(),
      author='Arthur Skowronek',
      author_email='eisensheng@mailbox.org',
      url='https://github.com/eisensheng/kaviar',
      license='MIT License',
      packages=find_packages(include=('kaviar', )),
      include_package_data=True,
      install_requires=['six', 'namedlist', ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Logging',
      ])
