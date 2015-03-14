[program:jupyterhub]
command=/usr/bin/python3 -m jupyterhub
directory=/srv/jupyterhub
autostart=true
autorestart=true
startretries=3
stderr_logfile=/var/log/jupyterhub.err.log
stdout_logfile=/var/log/jupyterhub.out.log
user=root
ENVIRONMENT=GITHUB_CLIENT_ID={GITHUB_CLIENT_ID},GITHUB_CLIENT_SECRET={GITHUB_CLIENT_SECRET},OAUTH_CALLBACK_URL={OAUTH_CALLBACK_URL},CONFIGPROXY_AUTH_TOKEN={CONFIGPROXY_AUTH_TOKEN}
