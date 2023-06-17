"""
! 使用usort 可以自动排序本文件的导包顺序
# install
* pip install usort
# 直接排序导包
* usort format <path> [<path> ...]
# 给导包排序的指导
* usort diff <path> [<path> ...]
# 检查是否符合规范
* usort check <path> [<path> ...]

# todo 可以进行更高级的配置pyproject.toml 集成到pkg包管理中
!https://usort.readthedocs.io/en/stable/guide.html#configuration
"""


# future imports
from __future__ import annotations

import re
import sys

# standard library

from datetime import date, datetime, timedelta
from pathlib import Path
from unittest import expectedFailure, skip, TestCase

# third-party
import requests
from attr import dataclasses
