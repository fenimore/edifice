# Edifice Playbook

    ansible-playbook -i hosts site.yml -u root

This ansible playbook was created for a Digital Ocean instance with Ubuntu 18 LTS installed. The roles will likely work on a variety of other systems with little to no changes. The main playbook will create a new user, set up some basic security (passwordless SSH, ufw), install zsh/oh-my-zsh, install nginx, and run cerbot for TLS. It will also install my personal dotfiles and a couple web apps and my homepage.

Included are some other playbooks for other things.

## Personal Website...

This playbook includes my personal dotfiles and web applications, including my homepage.

### Requirements

1. A remote host with Ubuntu 18 LTS
2. The necessary SSH keys to connect to that host
3. Ansible installed (in a python virtualenv)

## Jitsi Playbook

    ansible-galaxy install systemli.letsencrypt
    ansible-galaxy install systemli.jitsi_meet
    ansible-playbook -i hosts -u root opticon.yml

## Mac Dev Set Up

    # requires x-code
    ansible-galaxy install geerlingguy.homebrew
    ansible-playbook -v -i hosts mac.yml -K
