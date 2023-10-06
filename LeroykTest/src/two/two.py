#!/usr/bin/python
# -*- coding: utf-8 -*-

from one.one import One


class Two(object):

    def __init__(self, Two=1) -> None:
        self.num = Two

    def run(self):
        O = One()
        O.run()
        print(self.num)