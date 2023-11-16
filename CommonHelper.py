#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : auto
@File           : CommonHelper.py
@Software       : PyCharm
@Time           : 2022-09-22 14:26
@Description    : 读取qss文件
"""


def read_qss(style):
    with open(style, "r") as f:
        return f.read()
