from invoke import task

from tasks.common import VENV_PREFIX


@task
def run(ctx):
    result = ctx.run(f"{VENV_PREFIX} pytest", pty=True, warn=True)
    if result.exited == 5:
        exit(0)


@task
def cov(ctx):
    ctx.run(f"{VENV_PREFIX} pytest --cov=src/ tests/", pty=True)
