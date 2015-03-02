import os
import sys
from fabric.api import *

env.hosts = [os.getenv('HATCH_API_URL')]

CODE_DIR = '/srv/hatch/api'

@task
def deploy(repo_uri=None):
    """
    Deploy latest version of Hatch API
    """
    if repo_uri is None:
        repo_uri = 'git@github.com:pietdaniel/hatch-back-end.git'
    with settings(warn_only=True):
        if run('test -d {}'.format(CODE_DIR)).failed:
            run('git clone {} {}'.format(repo_uri, CODE_DIR))
    with cd(CODE_DIR):
        run('fig stop')
        run('fig build')
        run('fig up -d db')
        local('sleep 5')
        run('fig up -d server')
        run('fig ps')
@task
def logs():
    with cd(CODE_DIR):
        run('fig logs')

def status():
    with cd(CODE_DIR):
        run('fig ps')

def stop():
    with cd(CODE_DIR):
        run('fig stop')

def dump_db():
    """
    Work in progress
    """
    dumpfile = "/tmp/dump-`date \"+%Y-%m-%d_%H-%M-%S\"`.tar"
    pg_dump_opts = '-h db -p 5432 -U postgres -F tar -v -d neuhatch'
    pg_dump = "exec pg_dump {} > {}".format(pg_dump_opts, dumpfile)
    cmd = "bash -c '{}'".format(pg_dump)
    # TODO: check for /dbdumps/, create if missing
    docker_cmd_opts = "-i --link db:db -v /dbdumps/:/tmp/ postgres:9.4"
    docker_cmd= "docker run {} {}".format(docker_cmd_opts, cmd)
    run(docker_cmd)

def restore_db(dumpfile=None):
    if dumpfile is None:
        puts("Nothing to do")
        sys.exit(0)
    pg_restore_opts = '-h db -p 5432 -U postgres -d neuhatch -F tar'
    pg_restore = 'exec pg_restore {} -v {}'.format(pg_restore_opts, dumpfile)
    cmd = "bash -c '{}'".format(pg_dump)
    docker_cmd_opts = '-i --link db:db -v /dbdumps/:/tmp/ postgres:9.4'
    docker_cmd = 'docker run {} {}'.format(docker_cmd_opts, cmd)
    run(docker_cmd)
