#!/usr/bin/env python3
# © 2017 qsuscs, TobiX

import os
import sys
from glob import glob

os.chdir(os.path.dirname(__file__))
exit = 0

for f in glob('dot.*'):
    dst = os.path.expanduser('~/' + f[3:])
    src = os.path.join(os.getcwd(), f)
    src_rel = os.path.relpath(src, os.path.dirname(dst))
    try:
        os.symlink(src_rel, dst)
    except FileExistsError:
        if not os.path.samefile(src, dst):
            print(src + " exists and does not link do " + dst)
            exit = 1

sys.exit(exit)
