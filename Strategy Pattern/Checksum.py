#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: Checksum.py
@time: 2019/5/16 上午11:12
@brief: checksum 的计算，各个项目的计算方式不同
'''


class Checksum:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def calc(self, list):
        pass


class Add(Checksum):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def calc(self, list):
        total = 0
        for item in list:
            total += item
        return total



class Xor(Checksum):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def calc(self, list):
        total = 0
        for item in list:
            total ^= item
        return total


class Project:
    def __init__(self, checktype):
        self.checktype = checktype

    def __del__(self):
        pass

    def calc(self, list):
        return self.checktype.calc(list)


nums = [0x23, 0x01, 0x34, 0x45]
type = Add()
project = Project(type)
res = project.calc(nums)

print("res : {:#X}".format(res))

