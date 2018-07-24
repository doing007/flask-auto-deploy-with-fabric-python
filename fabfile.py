import os

from invoke import Responder
from fabric import Connection, Config, task

"""
Author: Mohan
email: reddimohana@gmail.com
"""

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
def service(ctx, service, control):
    """
    Restart services. ex: fab service nginx [status|restart|start|stop]
    """
    con = connect()
    password = sudopass()
    results = sudouser(ctx, 'sudo systemctl --no-pager ' + control + ' ' + service)
    status(ctx, service)


def sudopass():
    sudopass = Responder(
        pattern=r'\[sudo\] password:',
        response=os.environ['PASSWORD'] + '\n'
    )
    return sudopass


@task
def check_port(ctx, port):
    """
    To check If port is being used or not
    """
    port_results = sudouser(ctx, 'lsof -i:' + port)
    print(port_results)


def sudouser(ctx, command):
    c = connect()
    password = sudopass()
    results = c.sudo(command, pty=True, watchers=[password])
    return results


@task
def deploy(ctx, branch):
    """
    Auto deploy the application into server and restarts the service and nginx server
    """
    # Deploy branch
    # Pull the latest code from branch
    # Install the requirements If any ex: pip install -r requirements.txt --ignore-installed
    #
    # rollback code If server is not running with latest code and If any errors in the code
    pass

@task
def init(ctx):
    """
    Prepare the Server to install dependencies and required system level libraries (Optional)
    """
    # Update the Ubuntu server with sudouser
    # install required Ubuntu packages usinf sudo apt install package ex: nginx, gunicorn...
    #
    pass


def rollback():
    print('Rollback')
    pass

@task
def disk_used(cnt):
    """
    Check the / disk space usage
    """
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
    # Getting my server info from my system env (I have already exported so I can access it)
    server_ip = os.environ['MY_SERVER']
    os_server = 'mohan@' + server_ip
    connection = Connection(host=os_server)
    return connection
