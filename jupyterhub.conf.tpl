[program:jupyterhub]
command=/usr/bin/python3 -m jupyterhub
directory=/srv/jupyterhub
autostart=true
autorestart=true
startretries=3
stderr_logfile=/var/log/jupyterhub.err.log
stdout_logfile=/var/log/jupyterhub.out.log
user=root
