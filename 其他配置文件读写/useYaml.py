#!/usr/bin/python
# -*- coding: utf-8 -*-


import yaml

with open(r"pip包构建\其他配置文件读写\config.yaml", "r") as config:
    cfg = yaml.safe_load(config)


print(cfg)
