#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : python_project
@File           : FileTypeError.py
@Software       : PyCharm
@Time           : 2022/10/24 19:59
@Description    : 本类主要是用于构造系统托盘退出的弹窗，主要是从系统托盘鼠标右击退出确认的功能：
"""
from os import path
from logging import info
from sys import argv, exit
from PyQt5.Qt import Qt, QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, qApp


class FileTypeError(QWidget):
    def __init__(self, main_win, parent=None):
        super(FileTypeError, self).__init__(parent)
        self.file_path = path.dirname(path.abspath(__file__))
        self.full_path = self.file_path.replace("\\", "/")
        self.ui = main_win
        self.setWindowTitle("文件类型错误")
        # 设置ICO
        self.setWindowIcon(QIcon('%s/pic/main.png' % self.full_path))
        # 设置对象名称
        self.setObjectName("MainWindow1")
        self.width = 320
        self.height = 140
        self.resize(self.width, self.height)
        self.setStyleSheet("#MainWindow1{border: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);}")
        self.setContentsMargins(0, 0, 0, 0)
        self.hbox_1 = QHBoxLayout()
        self.hbox_1.setSpacing(0)
        self.hbox_1.setContentsMargins(0, 0, 0, 0)
        self.hbox_2 = QHBoxLayout()
        self.hbox_2.setSpacing(0)
        self.hbox_2.setContentsMargins(0, 0, 0, 0)
        self.hbox_3 = QHBoxLayout()
        self.hbox_3.setSpacing(0)
        self.hbox_3.setContentsMargins(0, 0, 0, 0)
        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)

        label_0 = QLabel()
        label_0.setObjectName("label_0")
        label_0.setPixmap(QPixmap("%s/pic/main.png" % self.full_path))
        label_0.setMaximumSize(40, 40)
        label_0.setMinimumSize(40, 40)
        label_0.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label_0.setStyleSheet("#label_0{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);}")
        self.hbox_1.addWidget(label_0)

        label_1 = QLabel("文件类型错误")
        label_1.setObjectName("label_1")
        label_1.setMaximumSize(700, 40)
        label_1.setMinimumSize(120, 40)
        label_1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_1.setStyleSheet("#label_1{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 16px;font-family: SimHei;}")
        self.hbox_1.addWidget(label_1)

        self.button_1 = QPushButton()
        self.button_1.setText("×")
        self.button_1.setToolTip("关闭")
        self.button_1.setObjectName("button_1")
        self.button_1.setMaximumSize(40, 40)
        self.button_1.setMinimumSize(40, 40)
        self.button_1.setStyleSheet("#button_1{border-bottom: 1px solid rgba(231, 233, 237, 1);border-left: 0px;border-top: 0px;border-right: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-size:20px;font-family:SimHei;vertical-align: middle;}#button_1:hover{background-color: rgb(251,115,115);}")
        self.button_1.pressed.connect(self.close_win)
        self.hbox_1.addWidget(self.button_1, Qt.AlignRight)
        self.vbox.addLayout(self.hbox_1)

        label_6 = QLabel()
        label_6.setObjectName("label_6")
        label_6.setMaximumSize(10, 40)
        label_6.setMinimumSize(10, 40)
        label_6.setAlignment(Qt.AlignCenter)
        label_6.setStyleSheet("#label_6{border: 1px solid rgba(0,0,0,0);border-radius:15px;margin-right: 0px;margin-left: 0px;margin-top: 10px;margin-bottom: 0px;padding: 0px;background-color: rgb(246,246,246);color: rgb(0,0,0);font-weight: bold;text-align: center;font-size: 18pt;font-family: Microsoft YaHei;}")
        self.hbox_2.addWidget(label_6)

        label_3 = QLabel()
        label_3.setText("!")
        label_3.setObjectName("label_3")
        label_3.setMaximumSize(25, 32)
        label_3.setMinimumSize(25, 32)
        label_3.setAlignment(Qt.AlignCenter)
        label_3.setStyleSheet("#label_3{border: 0px solid rgba(0,0,0,0);border-radius:12px;margin-right: 0px;margin-left: 0px;margin-top: 7px;margin-bottom: 0px;padding: 0px;background-color: rgba(255,77,79,1);color: rgb(0,0,0);font-weight: bold;text-align: center;font-size: 18px;font-family: Microsoft YaHei;}")
        self.hbox_2.addWidget(label_3)

        label_5 = QLabel()
        # 设置行间距
        label_5.setText("<p style='line-height:120%'>您选择文件类型不是：txt、xlsx、xls。\n请重新选择正确的文件类型！</p>")
        # 自动换行设置
        label_5.setWordWrap(True)
        font_1 = QFont()
        # 设置字间距
        font_1.setLetterSpacing(QFont.PercentageSpacing, 108)
        label_5.setFont(font_1)
        label_5.adjustSize()
        label_5.setObjectName("label_5")
        label_5.setMaximumSize(700, 60)
        label_5.setMinimumSize(150, 60)
        label_5.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_5.setStyleSheet("#label_5{border:0px;margin-right: 0px;margin-left: 10px;margin-top: 10px;margin-bottom: 0px;padding: 0px;background-color: rgb(246,246,246);color: rgb(0,0,0);text-align: center;font-size: 14px;font-family: Microsoft YaHei;}")
        self.hbox_2.addWidget(label_5)
        self.vbox.addLayout(self.hbox_2)

        label_2 = QLabel()
        label_2.setObjectName("label_2")
        label_2.setMaximumSize(700, 10)
        label_2.setMinimumSize(120, 10)
        label_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_2.setStyleSheet("#label_2{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 16px;font-family: SimHei;}")
        self.vbox.addWidget(label_2)

        self.label_3 = QLabel()
        self.label_3.setMaximumSize(620, 42)
        self.label_3.setMinimumSize(150, 42)
        self.hbox_3.addWidget(self.label_3, Qt.AlignCenter | Qt.AlignVCenter)

        self.button_3 = QPushButton("确 定")
        self.button_3.setMaximumSize(88, 45)
        self.button_3.setMinimumSize(88, 45)
        self.button_3.pressed.connect(self.close_win)
        self.button_3.setStyleSheet("QPushButton{border-radius: 5px;border: 0px;margin-top: 12px;margin-bottom: 0px;margin-right: 20px;margin-left: 0px;padding: 0px;background-color: rgb(20,108,185,180);vertical-align: middle;text-align: center;font-size: 14px;font-family: SimHei;color: rgb(255,255,255);}""QPushButton:hover{background-color: rgb(5,186,251,180);}""QPushButton:pressed{background: black;border: None;}")
        self.hbox_3.addWidget(self.button_3, Qt.AlignRight | Qt.AlignVCenter)
        self.vbox.addLayout(self.hbox_3)

        label_4 = QLabel()
        label_4.setMaximumSize(620, 15)
        label_4.setMinimumSize(120, 15)
        label_4.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(label_4, Qt.AlignCenter)
        self.setLayout(self.vbox)
        # 整个应用的透明设置,1.0最不透明
        self.setWindowOpacity(1.0)
        # 去掉窗口标题栏、任务栏边，且窗口置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def close_win(self):
        """
        :title 关闭程序(槽)
        :return: None
        """
        info("文件类型错误弹窗关闭！")
        self.close()
        self.ui.setEnabled(True)
        self.ui.showNormal()
        self.ui.activateWindow()
        self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.ui.show()


if __name__ == "__main__":
    app1 = QApplication(argv)
    form = FileTypeError("")
    form.show()
    exit(app1.exec_())
