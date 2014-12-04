from invoke import run, task
from textwrap import dedent

from tox._config import parseconfig


@task
def mktravisconfig():
    t = dedent("""\
        language: python
        python: 3.4
        env:
        {environs}
        install:
            - pip install tox setuptools==7.0
        script:
            - tox -e $TOX_ENV
    """)
    environs = ('\n'.join(('    - TOX_ENV=' + env)
                          for env in parseconfig(None, 'tox').envlist
                          if not env.startswith('cov-')))
    print(t.format(environs=environs))
