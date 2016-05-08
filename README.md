# JupyterHub demo

These are the setup scripts for a demo deployment of JupyterHub,
using GitHub OAuth and Docker spawning.
It is currently running at https://demohub.jupyter.org

## Clone and install JupyterHub and dependencies

    git clone https://github.com/jupyter/jupyterhub-demo /srv/jupyterhub
    cd /srv/jupyterhub
    make install

## Configure your deployment

1. write `userlist`, in the form:

        mal admin
        zoe admin
        inara admin
        wash
        kaylee
        jayne
        book
        simon
        river
   Admin users will have admin access to the JupyterHub instance. 
   See `userlist.example` for an example.

2. set up [GitHub OAuth][] and put the variables in `env`. See `env.example` for an example.
   The `OAUTH_CALLBACK_URL` will want to be of the form `https://YOURDOMAIN/hub/oauth_callback`

3. add your ssl cert and key in `ssl/ssl.crt` and `ssl/ssl.key`, respectively.

4. edit docker/Dockerfile as appropriate, then:

       make build

5. edit `jupyterhub_config.py` as appropriate

## Start and stop JupyterHub

This sets up JupyterHub with supervisor, so you use `supervisorctl` to stop and start the service:

    supervisorctl start jupyterhub

See supervisor docs for details on managing services.


[GitHub OAuth]: https://github.com/settings/applications/new