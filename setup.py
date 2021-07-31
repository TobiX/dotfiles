#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2017-2021 qsuscs, TobiX
# Should still run with Python 2.7...

from __future__ import print_function, unicode_literals

import os
import sys
from glob import glob

os.chdir(os.path.dirname(os.path.abspath(__file__)))
home = os.path.realpath(os.path.expanduser('~'))

exit = 0

for f in glob('dot.*'):
    dst_home = f[3:].replace("--", "\ufffd").replace("-", "/").replace("\ufffd", "-")
    dst = home + '/' + dst_home
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
        if not os.path.exists(dst):
            print('"{}" is a broken link pointing to "{}", replacing.'.format(
                dst_home, os.readlink(dst)))
            os.remove(dst)
            os.symlink(src_rel, dst)
        elif not os.path.samefile(src, dst):
            print('"{}" exists and does not link to "{}".'.format(dst_home, f))
            exit = 1

sys.exit(exit)
