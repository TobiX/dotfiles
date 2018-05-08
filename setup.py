#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2017-2018 qsuscs, TobiX
# Should still run with Python 2.7...

from __future__ import print_function, unicode_literals

import os
import sys
from glob import glob

os.chdir(os.path.dirname(os.path.abspath(__file__)))
exit = 0

for f in glob('dot.*'):
    dst = os.path.expanduser(
        '~/' + f[3:].replace("--", "\ufffd").replace("-", "/").replace("\ufffd", "-"))
    src = os.path.join(os.getcwd(), f)
    src_rel = os.path.relpath(src, os.path.dirname(dst))

    try:
        os.makedirs(os.path.dirname(dst))
    except OSError:
        pass

    try:
        os.symlink(src_rel, dst)
    except OSError:
        # Broken symbolic links do not "exist"
        if not os.path.exists(dst) or not os.path.samefile(src, dst):
            print(dst + " exists and does not link do " + src)
            exit = 1

sys.exit(exit)
