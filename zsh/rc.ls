# Colors and aliases for ls/exa

case `ls --version 2>/dev/null` in
	(*Free Software Foundation*)
		case $TERM in
			(screen*) eval `TERM=screen dircolors -b`;;
			(rxvt*) eval `TERM=rxvt dircolors -b`;;
			(*) eval `dircolors -b`;;
		esac
		alias ls='ls --color=auto -v'
		;;
	(*)
		export CLICOLOR=1 # FreeBSD, Darwin
		;;
esac

if [[ -x =exa ]]
then
	alias ls='exa'
	alias ll='exa -la'
	alias la='exa -a'
	alias l='exa -l'
	if [[ ! -x =tree ]]
	then
		alias tree='exa --tree'
	fi
else
	alias ll='ls -la'
	alias la='ls -A'
	alias l='ls -l'
fi

# vim: set ft=zsh ts=4 sw=4:
