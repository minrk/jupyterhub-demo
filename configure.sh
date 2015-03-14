#!/bin/bash
# configure the environment

# stage supervisord config file and reload
source ./env
./render jupyterhub.conf.tpl > /etc/supervisor/conf.d/jupyterhub.conf
supervisorctl reread
supervisorctl update
