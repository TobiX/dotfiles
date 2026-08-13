# Global Order: zshenv, zprofile, zshrc, zlogin
DEBIAN_PREVENT_KEYBOARD_CHANGES=true
# preload path for remote SSH commands
[[ -d ~/.local/bin ]] && path=(~/.local/bin $path)
