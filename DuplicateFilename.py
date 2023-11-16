#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : auto
@File           : DuplicateFilename.py
@Software       : PyCharm
@Time           : 2022-10-28 9:47
@Description    : 
"""
from os import path
from logging import info
from sys import argv, exit
from PyQt5.Qt import Qt, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton


class DuplicateFilename(QWidget):
    def __init__(self, main_win, parent=None):
        super(DuplicateFilename, self).__init__(parent)
        self.file_path = path.dirname(path.abspath(__file__))
        self.full_path = self.file_path.replace("\\", "/")
        self.ui = main_win
        self.setWindowTitle("日志文件异常")
        # self.setToolTip("日志文件异常")
        # 设置ICO
        self.setWindowIcon(QIcon('%s/pic/main.png' % self.full_path))
        # 设置对象名称
        self.setObjectName("MainWindow1")
        self.width = 384
        self.height = 120
        self.resize(self.width, self.height)
        self.setStyleSheet("#MainWindow1{border:0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);}")
        self.setContentsMargins(0, 0, 0, 0)
        self.hbox_1 = QHBoxLayout()
        self.hbox_1.setSpacing(0)
        self.hbox_1.setContentsMargins(0, 0, 0, 0)
        self.hbox_2 = QHBoxLayout()
        self.hbox_2.setSpacing(0)
        self.hbox_2.setContentsMargins(0, 0, 0, 0)
        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)

        label_0 = QLabel()
        label_0.setText("!")
        label_0.setAlignment(Qt.AlignCenter)
        label_0.setObjectName("label_0")
        label_0.setMaximumSize(55, 52)
        label_0.setMinimumSize(55, 52)
        label_0.setStyleSheet("#label_0{border: 0px;border-radius:10px;margin-top: 22px;margin-left: 20px;margin-right: 15px;margin-bottom: 10px;padding: 0px;background-color: rgba(255,77,79,1);font-weight: bold;color: rgb(255,255,255,255);text-align: center;font-size: 16px;font-family: SimHei;}")
        self.hbox_1.addWidget(label_0)

        font_1 = QFont()
        # 设置字间距
        font_1.setLetterSpacing(QFont.PercentageSpacing, 108)
        label_1 = QLabel("未获取到日志文件")
        label_1.setFont(font_1)
        label_1.setObjectName("label_1")
        label_1.setMaximumSize(700, 40)
        label_1.setMinimumSize(120, 40)
        label_1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_1.setStyleSheet("#label_1{border:0px;margin-right: 0px;margin-left: 0px;margin-top: 10px;margin-bottom: 0px;padding: 0px;background-color: rgb(246,246,246,255);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 16px;font-family: Microsoft YaHei;}")
        self.hbox_1.addWidget(label_1)

        self.button_1 = QPushButton()
        self.button_1.setText("×")
        self.button_1.setToolTip("关闭")
        self.button_1.setObjectName("button_1")
        self.button_1.setMaximumSize(40, 52)
        self.button_1.setMinimumSize(40, 52)
        self.button_1.setStyleSheet("#button_1{border: 0px;margin-left: 0px;margin-top: 0px;margin-right: 0px;margin-bottom: 12px;padding: 0px;background-color: rgb(246,246,246);font-size:20px;font-family:SimHei;vertical-align: middle;}#button_1:hover{background-color: rgb(251,115,115);}")
        self.button_1.pressed.connect(self.close_win_3)
        self.hbox_1.addWidget(self.button_1, Qt.AlignRight | Qt.AlignTop)
        self.vbox.addLayout(self.hbox_1)

        label_2 = QLabel()
        # 设置行间距
        label_2.setText("<p style='line-height:120%'> 未获取到日志文件，详细情况请咨询技术人员！</p>")
        # 自动换行设置
        label_2.setWordWrap(True)
        font_2 = QFont()
        # 设置字间距
        font_2.setLetterSpacing(QFont.PercentageSpacing, 108)
        label_2.setFont(font_2)
        label_2.adjustSize()
        label_2.setObjectName("label_1")
        label_2.setMaximumSize(700, 75)
        label_2.setMinimumSize(120, 50)
        label_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_2.setStyleSheet("#label_1{border:0px;margin-right: 32px;margin-left: 58px;margin-top: 0px;margin-bottom: 24px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(140,146,154);text-align: center;font-size: 14px;font-family: Microsoft YaHei;}")
        self.vbox.addWidget(label_2)

        self.vbox.addLayout(self.hbox_2)
        self.vbox.addLayout(self.hbox_2)
        self.setLayout(self.vbox)
        # 整个应用的透明设置,1.0最不透明
        self.setWindowOpacity(1.0)
        # 去掉窗口标题栏、任务栏边，且窗口置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def close_win_3(self):
        """
        :title 关闭程序(槽)
        :return: None
        """
        info("日志文件异常弹窗关闭！")
        self.close()
        self.ui.setEnabled(True)
        self.ui.showNormal()
        self.ui.activateWindow()
        self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.ui.show()


if __name__ == "__main__":
    app1 = QApplication(argv)
    form = DuplicateFilename("")
    form.show()
    exit(app1.exec_())
