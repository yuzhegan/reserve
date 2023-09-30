# encoding='utf-8

# @Time: 2023-09-30
# @File: %
#!/usr/bin/env
from icecream import ic
import os

import ddddocr

class GeneralOcr():
    def __init__(self, slideImg, bgImg):
        self.sildeImg = slideImg
        self.bgImg = bgImg
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

        with open(self.sildeImg, 'rb') as f:
            self.target_bytes = f.read()

        with open(self.bgImg, 'rb') as f:
            self.background_bytes = f.read()

        self.res = det.slide_match(self.target_bytes, self.background_bytes, simple_target=True)

# a = GeneralOcr('./dangdang/aa.png', './dangdang/bb.jpg').res['target'][0]
# print(a)

