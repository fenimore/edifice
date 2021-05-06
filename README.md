# Edifice(s)

Ansible Playbooks I use to configure remote and local hosts.

To set up the initial Debian server:

    ansible-playbook -i hosts site.yml -u root

This ansible playbook was created for a Digital Ocean instance with Ubuntu 18 LTS installed. The `common`, `nginx`, `apps`, and `minio` roles will work with Debian.

The `common` playbook will create a new user, set up some basic security (passwordless SSH, ufw), install zsh/oh-my-zsh and my dotfiles.

The `nginx`, `minio`, and `apps` roles will install nginx, run cerbot for TLS, and install a couple personal apps and my homepage.

The 'raspberrypi', `mac`, `jitsi`, and `raspberrypi` playbooks do other random things.

## Personal Website

Add a `vars/main.yml` variables file (using the `vars/default.yml`).

Debian compatible playbook:

    ansible-playbook -i hosts site.yml -u root

## RaspberryPi

Add a `vars/secrets.yml` variables file (leave empty to skip spotify configuration).

Raspbian (Debian) playbook:

    touch vars/secrets.yml  # add spotify username and password
    ansible-playbook -i hosts raspberrypi.yml --tags=pi

## Jitsi Playbook

Debian compatible playbook

    ansible-galaxy install systemli.letsencrypt
    ansible-galaxy install systemli.jitsi_meet
    ansible-playbook -i hosts -u root opticon.yml

## Mac Dev Set Up

Localhost playbook for MacOS

    # requires x-code
    ansible-galaxy install geerlingguy.homebrew
    ansible-playbook -v -i hosts mac.yml -K
