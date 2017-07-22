# TobiX’ .dotfiles

There are many git repositories full of dotfiles, but these are mine. If you
see something you like, take it (all my stuff is licensed under the ISC
license, see LICENSE for details). Be aware that there might be other people's
code included, but it should be clearly marked as such. This license also
doesn't cover other repositories included via git submodules - see those
repositories for the correct licensing terms.

## Subdirectories

To keep things simple, dotfiles in subdirectories are deployed by replacing
the slash in the filename with U+2571 - a unicode box drawing symbol (╱)

## Compatiblity

These files are used on Linux systems most of the time. Once upon a time, the
shell init stuff was compatible with Solaris, but it might not be anymore...
BSD compatibility seems to be fine, but is less tested.

The zsh init scripts should be compatible with a wide range of zsh versions.

## How to install

```
git clone --recursive https://github.com/TobiX/dotfiles.git
cd dotfiles
./setup.py  # or python setup.py
```

# Credits

- @qsuscs for his dead-simple dotfiles setup script.
- Sven Guckes for his screenrc.
