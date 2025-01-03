#!/usr/bin/env python3
# coding: utf-8

"""
compose url into qrcode
"""

import os
import sys

from testqr import get_qrcode


def main(argv):
    """main"""

    if argv == []:
        argv.append("2330")

    for stockid in argv:
        url = "https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID={}".format(
            stockid
        )
        print(url)
        get_qrcode(url)

        nfn = "goodinfo-{}.png".format(stockid)
        os.rename("image.png", nfn)
        print("rename as", nfn)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("goodinfo_qrcode.py [id] [id] ...")
        print("\ndemo mode...")
        main([])
        sys.exit(0)

    main(sys.argv[1:])
