# Colors and aliases for ls/eza

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

# exa is unmaintained, use maintained fork eza
if [[ -x =eza ]]
then
	alias ls='eza'
	alias ll='eza -la'
	alias la='eza -a'
	alias l='eza -l'
	if [[ ! -x =tree ]]
	then
		alias tree='eza --tree'
	fi
else
	alias ll='ls -la'
	alias la='ls -A'
	alias l='ls -l'
fi

# vim: set ft=zsh ts=4 sw=4:
