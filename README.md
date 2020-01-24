# Set Up Remote host With Nginx and Lets Encrypt


    ansible-playbook -i hosts site.yml -u root

This ansible playbook was created for a Digital Ocean instance with Ubuntu 18 LTS installed. The roles will likely work on a variety of other systems with little to no changes. This playbook will create a new user, set up some basic security (passwordless SSH, ufw), install zsh/oh-my-zsh, install nginx, and run cerbot for TLS.

```
roles/
├── common
│   ├── handlers
│   │   └── main.yml
│   ├── tasks
│   │   ├── main.yml
│   │   └── zsh.yml
│   └── templates
│       └── zshrc.tpl
└── nginx
    ├── handlers
    │   └── main.yml
    ├── tasks
    │   ├── letsencrypt.yml
    │   └── main.yml
    └── templates
        ├── certbot.conf.tpl
        ├── nginx.conf.tpl
        └── site-default.tpl
```

## Requirements

1. A remote host with Ubuntu 18 LTS
2. The necessary SSH keys to connect to that host
3. Ansible installed (in a python virtualenv)