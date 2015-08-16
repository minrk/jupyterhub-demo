# Configuration file for Jupyter Hub

c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.container_image = 'singleuser'

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from IPython.utils.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.JupyterHub.proxy_cmd = ['configurable-http-proxy', '--redirect-port', '80']


# OAuth with CILogon
c.JupyterHub.authenticator_class = 'oauthenticator.cilogon.CILogonOAuthenticator'

c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()

c.JupyterHub.admin_access = True

import os

join = os.path.join
here = os.path.dirname(__file__)

with open(join(here, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)

# ssl config
ssl = join(here, 'ssl')
keyfile = join(ssl, 'ssl.key')
certfile = join(ssl, 'ssl.crt')
if os.path.exists(keyfile):
    c.JupyterHub.ssl_key = keyfile
if os.path.exists(certfile):
    c.JupyterHub.ssl_cert = certfile
    c.JupyterHub.port = 443
