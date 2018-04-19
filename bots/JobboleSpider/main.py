# -*- coding: utf-8 -*-
# @Time    : 29/8/17 15:28
__author__ = 'guoping'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
