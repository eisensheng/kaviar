from invoke import run, task
from textwrap import dedent

from tox._config import parseconfig


@task
def mk_travis_config():
    """Generate configuration for travis."""
    t = dedent("""\
        language: python
        python: 3.4
        env:
        {jobs}
        install:
            - pip install -r requirements/ci.txt
        script:
            - invoke ci_run_job $TOX_JOB
        after_success:
            coveralls
    """)
    jobs = [env for env in parseconfig(None, 'tox').envlist
            if not env.startswith('cov-')]
    jobs += 'coverage',
    print(t.format(jobs=('\n'.join(('    - TOX_JOB=' + job)
                                   for job in jobs))))


@task
def ci_run_job(job_name):
    """Run given job name in tox environment.  This task is supposed to run
    within the CI environment.
    """
    run(('tox'
         + ((' -e ' + job_name) if job_name != 'coverage' else '')
         + ' -- --color=yes'),
        pty=True)
