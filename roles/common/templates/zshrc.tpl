# Path to oh-my-zsh installation.
export ZSH=/home/{{ personal_user }}/.oh-my-zsh

DISABLE_UPDATE_PROMPT=true  # auto updates

# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"
plugins=(
  git
  zsh-autosuggestions
)
source $ZSH/oh-my-zsh.sh
