#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : auto
@File           : LogGeneration.py
@Software       : PyCharm
@Time           : 2023-02-02 10:08
@Description    :
"""
from os import path
from logging import getLogger, INFO, FileHandler, StreamHandler, Formatter


def display_and_save_logs(log_path):
    """
    :title 既能把生成的日志保存到日志文件中，也能把生成的日志显示在控制台
    :param log_path:保存日志文件的完整路径
    :return: None
    """
    if not path.exists(log_path):
        open(log_path, "a+", encoding="utf-8")
    else:
        log_path = log_path
    # 创建一个logger
    logger = getLogger()
    logger.setLevel(INFO)
    # 创建一个handler,用于写入日志文件
    fh = FileHandler(log_path)
    fh.setLevel(INFO)
    # 再创建一个handler,用于输出到控制台
    ch = StreamHandler()
    ch.setLevel(INFO)
    # 定义handler的输出格式
    formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
