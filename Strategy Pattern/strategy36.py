#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: strategy36.py
@time: 2019/5/16 上午10:26
@brief:
'''

class Strategy:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def make_plan(self):
        pass


class KongCheng(Strategy):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def make_plan(self):
        print("空城计")


class Meiren(Strategy):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def make_plan(self):
        print("美人计")


class Liu(Strategy):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def make_plan(self):
        print("走为上策")


class ZhuGeLiang:
    def __init__(self, strategy):
        self.strategy = strategy

    def __del__(self):
        pass

    def give_addvice(self):
        self.strategy.make_plan()


plan = Meiren()
zgl = ZhuGeLiang(plan)

zgl.give_addvice()


