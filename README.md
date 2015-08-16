# JupyterHub demo (CILogon)

These are the setup scripts for a demo deployment of JupyterHub,
using CILogon OAuth and Docker spawning.
It is currently running at https://cilogon-hub.jupyter.org

## Clone and install JupyterHub and dependencies

    git clone https://github.com/minrk/jupyterhub-demo -b cilogon /srv/jupyterhub
    cd /srv/jupyterhub
    sh install.sh

## Configure your deployment

1. write `userlist`, in the form:

        mal.lbl.gov admin
        zoe.ucsd.edu admin
        inara.xsede.org admin
        wash.hotmail.com
        kaylee.gmail.com
   Admin users will have admin access to the JupyterHub instance. 
   See `userlist.example` for an example.

2. set up [CILogon OAuth][] (see below) and put the variables in `env`. See `env.example` for an example.
    - `OAUTH_CALLBACK_URL` will have the form `https://YOURDOMAIN/hub/oauth_callback`
    - `CILOGON_CLIENT_ID` will be the client ID from CILogon
    - `CILOGON_RSA_KEY_PATH` will be the path to the private RSA key file
    - `CILOGON_CSR_PATH` will be the path to the CSR file

3. add your ssl cert and key in `ssl/ssl.crt` and `ssl/ssl.key`, respectively.

4. apply your configuration:

        ./configure.sh

5. edit `jupyterhub_config.py` as appropriate


## Start and stop JupyterHub

This sets up JupyterHub with supervisor, so you use `supervisorctl` to stop and start the service:

    supervisorctl start jupyterhub

See supervisor docs for details on managing services.


## Setting up CILogon OAuth:

[Reference doc][CILogon OAuth]

1. generate rsa keypair:

        openssl genrsa -out oauth-privkey.pem 2048
        openssl rsa -in oauth-privkey.pem -pubout -out oauth-pubkey.pem
    JupyterHub will find the private key with `CILOGON_RSA_KEY_PATH` env

2. generate certificate request (interactive)

        openssl req -new -key oauth-privkey.pem -out oauth-cert.csr
    JupyterHub will find this file with `CILOGON_CSR_PATH` env

3. register with CILogon: https://cilogon.org/oauth/register
4. save your client_id from the request.
    JupyterHub will find this in `CILOGON_CLIENT_ID` env.

Caveats:

- For user whitelist/admin names,
  usernames will be email addresses where '@' is replaced with '.'
  
[CILogon OAuth]: http://grid.ncsa.illinois.edu/myproxy/oauth/client/manuals/registering-with-a-server.xhtml