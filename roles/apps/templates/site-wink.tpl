server {
  listen 80;
  listen [::]:80;

  listen [::]:443 ssl ipv6only=on; # managed by Ansible from Certbot
  listen 443 ssl; # managed by Ansible from Certbot
  #include conf/001-certbot.conf;  # managed, added by ansible from Certbot

  root /var/www/html;

  index index.html index.htm index.php;

  server_name {{ domain }} www.{{domain}};


  location / {
    # First attempt to serve request as file, then
    # as directory, then fall back to displaying a 404.
    try_files $uri $uri/ =404;
  }

  location /wink/wink.ini { internal;}

  location ~ \.php$ {
           include snippets/fastcgi-php.conf;
           fastcgi_pass unix:/run/php/php7.2-fpm.sock;
  }
}
