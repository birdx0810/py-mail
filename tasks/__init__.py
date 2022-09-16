from invoke import Collection

from tasks import env, git, lint, test

ns = Collection()
ns.add_collection(env)
ns.add_collection(git)
ns.add_collection(test)
ns.add_collection(lint)
