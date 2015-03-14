#!/bin/bash
# configure the environment

# stage supervisord config file and reload
./render_env jupyterhub.conf.tpl env > /etc/supervisor/conf.d/jupyterhub.conf
supervisorctl reread
supervisorctl update
