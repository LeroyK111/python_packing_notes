#!/usr/bin/python
# -*- coding: utf-8 -*-


class One(object):

    def __init__(self, one=1) -> None:
        self.num = one

    def run(self):
        print(self.num)