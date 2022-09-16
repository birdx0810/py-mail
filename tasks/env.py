from invoke import task

from tasks.common import VENV_PREFIX


@task
def clean(ctx):
    """Remove virtual environment"""
    ctx.run("pipenv --rm", warn=True)


@task
def init(ctx, e="dev"):
    """Install virtual environment (default: dev)"""
    ctx.run("pyenv install 3.10.4")
    ctx.run("pyenv local 3.10.4")
    

    if e.startswith("prod"):
        ctx.run("pipenv install --deploy")
    else:
        ctx.run("pipenv install --dev")
        ctx.run("git init")
        ctx.run("git config user.name Daniel Tan")
        ctx.run("git config user.email birdx0810@gmail.com")
        ctx.run("git remote set-url origin https://github.com/birdx0810/py-mail")
        ctx.run(f"{VENV_PREFIX} pre-commit install -t pre-commit")
        ctx.run(f"{VENV_PREFIX} pre-commit install -t pre-push")
        ctx.run(f"{VENV_PREFIX} pre-commit install -t commit-msg")
        ctx.run(f"{VENV_PREFIX} pre-commit autoupdate")
