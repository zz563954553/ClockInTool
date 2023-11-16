#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : python_project
@File           : NewPushButton.py
@Software       : PyCharm
@Time           : 2022/10/24 21:36
@Description    : 重写QPushButton，新增拖拽txt/xlsx/xls类文件到按钮区域，按钮显示显示完整文件路径
"""
from logging import info, error
from PyQt5.QtWidgets import QPushButton
from FileTypeError import FileTypeError


class NewPushButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
        self.parent = parent
        self.file_type_error = FileTypeError(parent)

    def dragEnterEvent(self, event):
        """
        :title 重写拖拽进入规定内区域事件
        :return: None
        """
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """
        :title 重写拖拽事件，识别到拖拽文件后，拿到文件完整路径，在判断文件类型是否符合规则
        :return: None
        """
        try:
            pre_path = event.mimeData().text()
            full_path = pre_path.split("file:///")[1]
            if ".txt" in full_path:
                self.setText("\n点击或拖拽文件到此虚线区域上传\n此版本支持上传文件的扩展名：.xls .xlsx .txt\n拖入文件的完整路径为：\n%s" % full_path)
                self.setToolTip(full_path)
                info("拖入文件为txt文件，其完整路径为：%s！" % full_path)
            elif ".xlsx" in full_path:
                self.setText("\n点击或拖拽文件到此虚线区域上传\n此版本支持上传文件的扩展名：.xls .xlsx .txt\n拖入文件的完整路径为：\n%s" % full_path)
                self.setToolTip(full_path)
                info("拖入文件为xlsx文件，其完整路径为：%s！" % full_path)
            elif ".xls" in full_path:
                self.setText("\n点击或拖拽文件到此虚线区域上传\n此版本支持上传文件的扩展名：.xls .xlsx .txt\n拖入文件的完整路径为：\n%s" % full_path)
                self.setToolTip(full_path)
                info("拖入文件为xls文件，其完整路径为：%s！" % full_path)
            else:
                info("拖入文件不符合规则，其完整路径为：%s！" % full_path)
                self.file_type_error.show()
                self.file_type_error.move(int(self.parent.pos().x() + (self.parent.width - self.file_type_error.width) / 2), int(self.parent.pos().y() + (self.parent.height - self.file_type_error.height) / 2))
                self.parent.setEnabled(False)
        except Exception as e:
            info("拖拽文件到控件NewPushButton区域内报错，具体原因如下所示！")
            error(e)
