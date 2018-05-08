# Colors and aliases for ls

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

alias ll='ls -la'
alias la='ls -A'
alias l='ls -l'

# vim: set ft=zsh ts=4 sw=4:
