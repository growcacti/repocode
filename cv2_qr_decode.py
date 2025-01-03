#!/usr/bin/env python3
# coding: utf-8

""" using opencv to decode qrcode """

import cv2
import common


def process(fn):
    """process"""
    image = cv2.imread(fn)
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, _, _ = qrCodeDetector.detectAndDecode(image)
    if decodedText:
        print(decodedText)


def main():
    """main"""
    for fn in common.get_pngs():
        process(fn)


if __name__ == "__main__":
    main()
