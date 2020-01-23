##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# http://wiki.nginx.org/Pitfalls
# http://wiki.nginx.org/QuickStart
# http://wiki.nginx.org/Configuration
#
# Generally, you will want to move this file somewhere, and start with a clean
# file but keep this around for reference. Or just disable in sites-enabled.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

# Default server configuration
#
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  listen [::]:443 ssl ipv6only=on; # managed by Ansible from Certbot
  listen 443 ssl;                  # managed by Ansible from Certbot

  # Note: You should disable gzip for SSL traffic.
  # See: https://bugs.debian.org/773332 TODO:

  root /var/www/html;

  index index.html

  server_name {{ domain }} www.{{domain}};

  location / {
    # First attempt to serve request as file, then
    # as directory, then fall back to displaying a 404.
    try_files $uri $uri/ =404;
  }
}
