import os

from invoke import Responder
from fabric import Connection, Config, task


@task
def status(ctx, service):
    """
    Find out the status of any service
    """
    con = connect()
    password = sudopass()
    results = con.sudo('sudo systemctl --no-pager status ' + service, pty=True, watchers=[password])
    return results


@task
def restart(ctx, service):
    """
    Restart services. ex: nginx, discovery..
    """
    con = connect()
    password = sudopass()
    results = con.sudo('sudo systemctl restart ' + service, pty=True, watchers=[password])
    status(ctx, service)


def sudopass():
    sudopass = Responder(
        pattern=r'\[sudo\] password:',
        response=os.environ['PASSWORD'] + '\n'
    )
    return sudopass


@task
def deploy(cmd):
    pass


@task
def disk_used(cnt):
    c = connect()
    result = c.run('uname -s', hide=True)
    uname = result.stdout.strip()
    if uname == 'Linux':
        command = "df -h / | tail -n1 | awk '{print $5}'"
        r = c.run(command, hide=True).stdout.strip()
        print(r)
    err = "No idea how to get disk space on {}!".format(uname)
    # raise Exit(err)


def connect():
    os_server = 'username@xx.xx.xx.xx'
    connection = Connection(host=os_server)
    return connection
