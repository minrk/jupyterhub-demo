# Configuration file for Jupyter Hub

c = get_config()

# spawn with Docker
from dockerspawner import DockerSpawner

import os

root_dir = os.path.dirname(__file__)
skeleton_home_dir = os.path.join(root_dir, 'skel')
import shutil

# uid, gid of docker user
uid = 1000
gid = 1000

c.DockerSpawner.remove_containers = True
class LocalDockerSpawner(DockerSpawner):
    def start(self):
        work_dir = os.path.join(root_dir, 'work', self.user.name)
        if not os.path.exists(work_dir):
            shutil.copytree(skeleton_home_dir, work_dir)
            os.chown(work_dir, uid, gid)
        return super().start()

c.JupyterHub.spawner_class = LocalDockerSpawner
c.DockerSpawner.container_image = 'singleuser'
c.DockerSpawner.volumes = {
    os.path.join(root_dir, 'work/{username}'): '/home/jovyan/work',
}

c.Spawner.default_url = '/lab'

# The docker instances need access to the Hub, so the default loopback port doesn't work:
import netifaces
docker_ip = netifaces.ifaddresses('docker0')[netifaces.AF_INET][0]['addr']
c.JupyterHub.hub_ip = docker_ip

c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--redirect-port', '80']
import binascii
c.ConfigurableHTTPProxy.api_url = 'http://127.0.0.1:50505'
c.ConfigurableHTTPProxy.auth_token = binascii.b2a_hex(os.urandom(16))


# OAuth with GitHub
c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'

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

c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# ssl config
ssl = join(here, 'ssl')
keyfile = join(ssl, 'ssl.key')
certfile = join(ssl, 'ssl.crt')
if os.path.exists(keyfile):
    c.JupyterHub.ssl_key = keyfile
if os.path.exists(certfile):
    c.JupyterHub.ssl_cert = certfile
    c.JupyterHub.port = 443
