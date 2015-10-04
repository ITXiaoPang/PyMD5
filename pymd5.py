#!/usr/bin/env python
#encoding:utf-8
import os
import sys
import hashlib


# get md5 of a input string
def getStrHash(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


# get md5 of a input bigfile
def getFileHash(my_file):
    m = hashlib.md5()
    f = open(my_file, 'rb')
    my_buffer = 1024 * 1024

    while True:
        buf = f.read(my_buffer)
        if not buf:
            break
        m.update(buf)

    f.close()
    return m.hexdigest()


def gethash(obj):
    if os.path.exists(obj):
        ret = getFileHash(obj)
    else:
        ret = getStrHash(obj)
    return ret


if __name__ == "__main__":
    for v in sys.argv:
        if not v == sys.argv[0]:
            print(v + ':' + gethash(v) + os.linesep)

