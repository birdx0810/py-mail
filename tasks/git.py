from invoke import task

from tasks.common import VENV_PREFIX


@task
def commit(ctx):
    ctx.run(f"{VENV_PREFIX} cz commit", pty=True)


@task
def bump(ctx, changelog=False):
    argument = ""
    if changelog:
        argument += "--changelog"

    result = ctx.run(f"{VENV_PREFIX} cz bump --yes {argument}".strip(), warn=True)

    if result.exited == 3:
        exit(0)
    else:
        exit(result.exited)
