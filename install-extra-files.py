#!/usr/bin/python3

import contextlib
import hashlib
import os
import os.path
import shutil
from urllib.request import urlopen


class File:
    def __init__(self, src, sha, dst):
        self.src = src
        self.sha = sha
        self.dst = os.path.expanduser('~/' + dst)

    def needsupdate(self):
        if not os.path.exists(self.dst):
            return True

        with open(self.dst, 'rb') as f:
            m = hashlib.sha256()
            for chunk in iter(lambda: f.read(4096), b''):
                m.update(chunk)
            return m.hexdigest() != self.sha

    def update(self):
        with contextlib.suppress(OSError):
            os.makedirs(os.path.dirname(self.dst))
        with open(self.dst, 'wb') as f:
            with urlopen(self.src) as s:
                shutil.copyfileobj(s, f)

    def dstname(self):
        return os.path.basename(self.dst)


FILES = [
    File('https://cdn.rawgit.com/ryanoasis/nerd-fonts/20429f277594fbf7704d2b3dfa0e55c9b7df457e/patched-fonts/Terminus/terminus-ttf-4.40.1/Regular/complete/Terminess%20(TTF)%20Nerd%20Font%20Complete%20Mono.ttf',
         '087ec7fe10f5b5c072a6979dd06218c3e05f9980b3743b322f4f90a7ee1186cc',
         '.local/share/fonts/Terminess (TTF) Nerd Font Complete Mono.ttf'),
    File('https://cdn.rawgit.com/ryanoasis/nerd-fonts/' +
         '20429f277594fbf7704d2b3dfa0e55c9b7df457e' +
         '/patched-fonts/Terminus/terminus-ttf-4.40.1/Regular/complete' +
         '/Terminess%20(TTF)%20Nerd%20Font%20Complete.ttf',
         '30a375a9528efb499691dc3a1f27eef29f919668562af796b563bafc55c41d1f',
         '.local/share/fonts/Terminess (TTF) Nerd Font Complete.ttf')
]

for f in FILES:
    if f.needsupdate():
        print('"%s" needs update, downloading...' % f.dstname())
        f.update()
