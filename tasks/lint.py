from invoke import task

from tasks.common import COMMON_TARGETS, VENV_PREFIX


@task
def black(ctx):
    ctx.run(f"{VENV_PREFIX} black {COMMON_TARGETS}")


@task
def isort(ctx):
    ctx.run(f"{VENV_PREFIX} isort --atomic .")


@task
def flake8(ctx):
    ctx.run(f"{VENV_PREFIX} flake8 --config=setup.cfg")


@task
def mypy(ctx):
    ctx.run(f"{VENV_PREFIX} mypy")


@task
def commit(ctx):
    result = ctx.run(f"{VENV_PREFIX} cz check --rev-range main..", warn=True)
    if result.exited == 3:
        exit(0)
    else:
        exit(result.exited)


@task(pre=[black, isort, flake8, mypy, commit])
def lint(ctx):
    """Lint all objects"""
    pass
