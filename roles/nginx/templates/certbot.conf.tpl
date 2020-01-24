# managed by Ansible for Certbot/Let's Encrypt

ssl_certificate /etc/letsencrypt/live/{{ domain }}/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/{{ domain }}/privkey.pem;
include /etc/letsencrypt/options-ssl-nginx.conf;
ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;