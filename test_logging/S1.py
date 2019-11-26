#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/27 11:17
# @Author : 不爱码代码的码农
# @Site : 
# @File : S1.py
# @Software: PyCharm
import logging
from logging import handlers


'''
输出log到控制台以及将日志写入log文件。
保存2种类型的log， all.log 保存debug, info, warning, critical 信息， error.log则只保存error信息，同时按照时间自动分割日志文件
'''
class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式

        # th = logging.FileHandler(filename=filename, mode='w', encoding='utf-8') 设置写入文件为覆盖模式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        if not self.logger.handlers: # 防止添加多个对象
            self.logger.addHandler(sh) #把对象加到logger里
            self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('all.log',level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    Logger('error.log', level='error').logger.error('error')