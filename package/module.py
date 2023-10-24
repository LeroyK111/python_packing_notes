#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
调用__init__.py中的变量和对象
"""
# 这就是同级别调用
from __init__ import info, testGlobal

print(info)
testGlobal()
