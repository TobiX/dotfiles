# TobiX’ .dotfiles

There are many git repositories full of dotfiles, but these are mine. If you
see something you like, take it (all my stuff is licensed under the ISC
license, see LICENSE for details). Be aware that there might be other people's
code included, but it should be clearly marked as such. This license also
doesn't cover stuff that may be downloaded by using this repository (for
example vim plugins) - look at their source for the correct licensing terms.

## Subdirectories

To keep things simple, dotfiles in subdirectories are deployed using a
replacement scheme similar to systemd's unit files: A single minus (-)
represents a slash in the target file name, while a minus can be escaped by
repeating it (--).

## Compatiblity

These files are used on Linux systems most of the time. Once upon a time, the
shell init stuff was compatible with Solaris, but it might not be anymore...
BSD compatibility seems to be fine, but is less tested.

The zsh init scripts should be compatible with a wide range of zsh versions.

## How to install

```
git clone https://github.com/TobiX/dotfiles.git
cd dotfiles
./setup.py  # or python setup.py
```

# Credits

- @qsuscs for his dead-simple dotfiles setup script.
- Sven Guckes for his screenrc.
