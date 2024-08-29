#!/usr/bin/python
# -*- coding: utf-8 -*-
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read(r"E:\code\pip包构建\其他配置文件读写\config.ini")
result = dict(cfg.items("localdb"))
print(result)
