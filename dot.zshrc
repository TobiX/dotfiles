# main zshrc loop
autoload -Uz colors
zmodload zsh/terminfo
if [[ $#terminfo -eq 0 ]]
then
	TERM=vt100
fi
if [[ $#terminfo -gt 0 && $terminfo[colors] -ge 8 ]]
then
	colors
fi

if [[ -x =doas ]]
then
	rootcmd=doas
else
	rootcmd=sudo
fi

__thiszshrc="${ZDOTDIR:-$HOME}/.zshrc"
export DOTFILES_BASE="$__thiszshrc:A:h"
unset __thiszshrc

setopt extended_glob
echo "$fg[green]starting up shell$reset_color\c"
[[ $V == 1 ]] && echo ":\c"
for script in $DOTFILES_BASE/zsh/rc.*~*~
do
	[[ $V == 1 ]] && echo " $script:e\c" || echo ".\c"
	. $script
	[[ $? -ne 0 ]] && { [[ $V == 1 ]] && echo "\e[$#script:eD$fg[red]$script:e$reset_color\c" || echo "\e[1D$fg[red].$reset_color\c" }
done
[[ $V == 1 ]] && echo "." || echo
unset script rootcmd

# vi: set ts=4 sw=4 ft=zsh:
