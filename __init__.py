

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
