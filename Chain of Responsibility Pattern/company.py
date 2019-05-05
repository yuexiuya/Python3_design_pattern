#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: company.py
@time: 2019/4/30 17:16
@brief: 责任链模式：公司流程
'''

from enum import IntEnum


class Event(IntEnum) :
    off_work = 0  # 请假
    pay_raise = 1  # 加薪
    leave = 2  # 离职
    buy_shares = 3  # 入股


class AbstractWork :
    def __init__(self) :
        self.level = Event.off_work
        self.nextManager = self

    def setNextManager(self, next_manager) :
        self.nextManager = next_manager

    def handle(self, level) :
        print("{0} do nothing ".format(self.__class__))


class HeadMan(AbstractWork) :
    def __init__(self) :
        self.level = Event.off_work
        self.nextManager = self

    def handle(self, level) :
        if level <= self.level :
            print("{0} handle ".format(self.__class__))
        else :
            self.nextManager.handle(level)


class Manager(AbstractWork) :
    def __init__(self) :
        self.level = Event.leave
        self.nextManager = self

    def handle(self, level) :
        if level <= self.level :
            print("{0} handle ".format(self.__class__))
        else :
            self.nextManager.handle(level)


class President(AbstractWork) :
    def __init__(self) :
        self.level = Event.buy_shares
        self.nextManager = self

    def handle(self, level) :
        if level <= self.level :
            print("{0} handle ".format(self.__class__))
        else :
            self.nextManager.handle(level)


def log_chain() :
    headman = HeadMan()
    manager = Manager()
    president = President()

    headman.setNextManager(manager)
    manager.setNextManager(president)
    president.setNextManager(president)

    return headman


log_chain().handle(Event.off_work)
log_chain().handle(Event.pay_raise)
log_chain().handle(Event.leave)
log_chain().handle(Event.buy_shares)
