import os
import sys
from invoke import Responder
from fabric import Connection, Config, task
from pprint import pprint
sys.path.append('/opt/settings')
import re
import config
# import logger as log
import logger
log = logger.Logger()
app_dir = '/opt'


"""
Author: Mohan
email: reddimohana@gmail.com
"""

global conf

@task
def test(ctx):
    """
    Test task
    """
    pass


@task
def status(ctx, env, service):
    """
    Find out the status of any service. ex: fab status [nginx|apache2|mongod]
    """
    con = connect(env)
    password = sudopass(env)
    results = con.sudo('sudo systemctl --no-pager status ' + service, pty=True, watchers=[password])
    return results

@task
def service(ctx, env, service, control):
    """
    Restart services. ex: fab service nginx [status|restart|start|stop]
    """
    con = connect(env)
    password = sudopass(env)
    results = sudorun(ctx, env, 'sudo systemctl --no-pager ' + control + ' ' + service)
    status(ctx, service)


def sudopass(env):
    sudopass = Responder(
        pattern=r'\[sudo\] password:',
        response=env['password'] + '\n'
    )
    return sudopass


@task
def deploy(ctx, env, branch):
    """
    Auto deploy the application into server and restarts the service and nginx server
    """
    # Deploy branch
    # Pull the latest code from branch
    # Install the requirements If any ex: pip install -r requirements.txt --ignore-installed
    # Display the nginx log error If any and roll back the changes
    # Check the PORT number, If it being used try the next port number
    # rollback code If server is not running with latest code and If any errors in the code
    # print(logger.__version__)
    c, e = connect(env)

    print(env)
    app_name, app_path = get_app_name(e['gitrepo'])
    sudorun(ctx, env, 'sudo mkdir ' + app_path + ' && sudo chown -R ' + e['user'] + ':' + e['user'] + ' ' + app_path)
    log.info("Created project dir " + app_path)

    log.info("Started cloning " + e['gitrepo'] + " to " + app_path)
    c.run("git clone " + e['gitrepo'] + " " + app_path)
    # sudorun(ctx, env, "git clone " + e['gitrepo'] + ' ./')
    pass

@task
def check_port(ctx, env, port):
    """
    To check If port is being used or not
    """
    port_results = sudorun(ctx, env, 'lsof -i:' + port)
    print(port_results)


def sudorun(ctx, env, command):
    c, env_conf = connect(env)
    password = sudopass(env_conf)
    log.debug(command)
    results = c.sudo(command, pty=True, watchers=[password])
    return results

def serviceList(ctx):
    """
    Get the list of services
    """
    # systemctl -l --type service --all
    pass

@task
def init(ctx):
    """
    Prepare the Server to install dependencies and required system level libraries (Optional)
    """
    # Update the Ubuntu server with sudorun
    # install required Ubuntu packages usinf sudo apt install package ex: nginx, gunicorn...
    #
    pass


def rollback():
    print('Rollback')
    pass

@task
def disk_used(cnt, env):
    """
    Check the / disk space usage
    """
    c = connect(env)
    result = c.run('uname -s', hide=True)
    uname = result.stdout.strip()
    if uname == 'Linux':
        command = "df -h / | tail -n1 | awk '{print $5}'"
        r = c.run(command, hide=True).stdout.strip()
        print(r)
    err = "No idea how to get disk space on {}!".format(uname)
    # raise Exit(err)
# def

def connect(env):
    env = env.upper()
    # Check If env config is available
    if env in config.SERVER:
        env_conf = config.SERVER[env]
    else:
        raise SystemExit(log.error(env + " configuration not found in configuration file"))
    # Getting my server info from my system env (I have already exported so I can access it)
    log.info("Connecting to " + env_conf['host'] + " server with " + env_conf['user'])
    os_server = env_conf['user'] + '@' + env_conf['host']
    connection = Connection(host=os_server)
    return connection, env_conf


def get_app_name(repo):
    regex = r".*\/(.*)\.git"
    name = ''
    matches = re.search(regex, repo, re.IGNORECASE)
    if matches:
        name = matches.group(1)

    return name, app_dir + '/' + name
