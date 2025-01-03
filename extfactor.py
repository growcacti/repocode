#!/usr/bin/env python3
# coding: utf-8

"""
    call /usr/bin/factor and pick results
    also refer to **factorint.py** that uses sympy to do factorize
"""

import os
from random import randint
import re
import sys
from myutil import read_from_stdin


def call_factor(n: int):
    """call external factor"""
    if n <= 0:
        print("{} cannot be zero or negative".format(n))
        return
    cmd = "/usr/bin/factor {}".format(n)
    a = os.popen(cmd).read()
    # print(res)
    b = re.sub(r"^(\d+: )(.+)$", "\\2", a.strip())
    vals = b.split(" ")
    print("{}: ".format(n), end="")
    if len(vals) == 1:
        print("a prime number")
    else:
        print(vals)


def main(argv):
    """main"""
    if argv == []:
        argv.append(randint(1001, 9999))

    for v in argv:
        try:
            call_factor(int(v))
        except ValueError:
            print("not a value:", v)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('use "{} -" read input from STDIN'.format(sys.argv[0]))
        # demo mode
        print("demo mode...")
        main([])
        sys.exit()

    if sys.argv[1] == "-":
        read_from_stdin(main)
    else:
        main(sys.argv[1:])
