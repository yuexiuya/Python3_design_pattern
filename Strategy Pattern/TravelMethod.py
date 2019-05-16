#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: TravelMethod.py
@time: 2019/5/16 上午11:03
@brief:
'''


class TravelMethod:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def transportation(self):
        pass


class Air(TravelMethod):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def transportation(self):
        print("by Air")


class Taxi(TravelMethod):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def transportation(self):
        print("by Taxi")


class Train(TravelMethod):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def transportation(self):
        print("by Train")


class Company:
    def __init__(self, type):
        self.type = type

    def __del__(self):
        pass

    def set_out(self):
        self.type.transportation()


air = Air()
company = Company(air)
company.set_out()