
# -*- coding: UTF-8 -*-
# //coding: utf-8
# coding=utf-8
# vim: set fileencoding=utf-8 :
print "Content-Type: text/html\r\n"
#~ print ("<meta charset="utf-8">")


import urllib2,json
import xmltodict
import locale,os
language, output_encoding = locale.getdefaultlocale()

from lxml import etree
from json2html import *


# 6.35
print('----')
