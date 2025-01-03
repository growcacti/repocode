#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""access_file test file existence before using it"""

import errno
import sys

try:
    import cv2
except ImportError:
    print("ImportError: pip install opencv-python")
    sys.exit()

# pylint: disable=no-member
# pylint: disable=consider-using-with


def test_file(fn: str) -> bool:
    """
    use open() to test file could be accessed
    """
    try:
        fp = open(fn)
    except IOError as e:
        if e.errno == errno.EACCES:
            print("errno: EACCES")
            return False
        # other than permission error
        if e.errno == errno.ENOENT:
            print("errno: ENOENT")
            return False
    else:
        fp.close()
        return True
    # should not be here?
    return False


def main(argv):
    """
    use cv2.imread() to load an image
    """
    if argv == []:
        fn = "/dev/shm/reid.jpg"
        print("specify an image file path, using default: %s" % fn)
        argv.append(fn)

    for f in argv:
        test_file(f)
        img = cv2.imread(f)
        if img is not None:
            print("press any key to continue, file:{}".format(f))
            cv2.imshow(f, img)
            cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])
