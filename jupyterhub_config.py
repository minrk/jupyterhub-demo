# Configuration file for JupyterHub

# OAuth with GitHub, creating local users if they don't exist
c.JupyterHub.authenticator_class = 'oauthenticator.github.LocalGitHubOAuthenticator'
c.LocalGitHubOAuthenticator.create_system_users = True

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
    # redirect http to https
    c.JupyterHub.proxy_cmd = ['configurable-http-proxy', '--redirect-port', '80']
    c.JupyterHub.ssl_cert = certfile
    c.JupyterHub.port = 443
