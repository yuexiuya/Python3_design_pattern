#!/usr/bin/env python
# encoding: utf-8
'''
@author: joshua
@license: 
@contact: hytmailforoffice@163.com
@software: 
@file: log_responsibility_chain.py
@time: 2019/4/22 17:00
@brief:  责任链模式：log
'''

from enum import Enum


class LogLevel(Enum) :
    INFO = 1
    DEBUG = 2
    WARN = 3
    ERROR = 4


class AbstractLogger :

    def __init__(self) :
        self.level = LogLevel.INFO
        self.nextLogger = self

    def setNextLogger(self, next_logger) :
        self.nextLogger = next_logger

    def log(self, level, message) :
        if level is self.level :
            print("{0}:{1}".format(level, message))
        else:
            if self.nextLogger != self :
                self.nextLogger.log(level, message)


class InfoLogger(AbstractLogger) :
    def __init__(self) :
        super().__init__()
        self.level = LogLevel.INFO
        self.nextLogger = self

    def log(self, level, message) :
        if level is self.level :
            print("Info : {0}".format(message))
        else:
            if self.nextLogger != self :
                self.nextLogger.log(level, message)


class DebugLogger(AbstractLogger) :
    def __init__(self) :
        super().__init__()
        self.level = LogLevel.DEBUG
        self.nextLogger = self

    def log(self, level, message) :
        if level is self.level :
            print("Debug : {0}".format(message))
        else:
            if self.nextLogger != self :
                self.nextLogger.log(level, message)


class WarnLogger(AbstractLogger) :
    def __init__(self) :
        super().__init__()
        self.level = LogLevel.WARN
        self.nextLogger = self

    def log(self, level, message) :
        if level is self.level :
            print("Warn : {0}".format(message))
        else:
            if self.nextLogger != self :
                self.nextLogger.log(level, message)


class ErrorLogger(AbstractLogger) :
    def __init__(self) :
        super().__init__()
        self.level = LogLevel.ERROR
        self.nextLogger = self

    def log(self, level, message) :
        if level is self.level :
            print("Error : {0}".format(message))
        else:
            print("xxx : ", id(self.nextLogger))
            print("xxx : ", id(self))
            if id(self.nextLogger) != id(self) :
                self.nextLogger.log(level, message)


def log_chain() :
    info_log = InfoLogger()
    debug_log = DebugLogger()
    warn_log = WarnLogger()
    err_log = ErrorLogger()

    info_log.setNextLogger(debug_log)
    debug_log.setNextLogger(warn_log)
    warn_log.setNextLogger(err_log)

    return info_log


log_chain().log(LogLevel.INFO, " This is a log")
log_chain().log(LogLevel.DEBUG, " This is a log")
log_chain().log(LogLevel.WARN, " This is a log")
log_chain().log(LogLevel.ERROR, " This is a log")
