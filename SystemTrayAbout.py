#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : python_project
@File           : SystemTrayAbout.py
@Software       : PyCharm
@Time           : 2022/10/24 17:28
@Description    : 用于构造系统托盘关于的弹窗，主要是版权声明
"""
from os import path
from sys import argv, exit
from logging import info, error
from PyQt5.Qt import Qt, QFont, QIcon, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton


class SystemTrayAbout(QWidget):
    def __init__(self, main_win, parent=None):
        super(SystemTrayAbout, self).__init__(parent)
        self.file_path = path.dirname(path.abspath(__file__))
        self.full_path = self.file_path.replace("\\", "/")
        self.ui = main_win
        self.setWindowTitle("关于消息定时发送工具")
        self.setToolTip("关于消息定时发送工具")
        # 设置ICO
        self.setWindowIcon(QIcon('%s/pic/main.png' % self.full_path))
        # 鼠标事件参数初始化
        self.m_flag = True
        self.m_position = None
        # 设置对象名称
        self.setObjectName("MainWindow1")
        self.width = 320
        self.height = 160
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
        label_0.setMaximumSize(40, 40)
        label_0.setMinimumSize(40, 40)
        label_0.setStyleSheet("#label_0{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);}")
        self.hbox_1.addWidget(label_0)

        label_1 = QLabel("关于")
        label_1.setObjectName("label_1")
        label_1.setMaximumSize(700, 40)
        label_1.setMinimumSize(120, 40)
        label_1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_1.setStyleSheet("#label_1{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 18px;font-family: SimHei;}")
        self.hbox_1.addWidget(label_1)

        self.button_1 = QPushButton()
        self.button_1.setText("×")
        self.button_1.setToolTip("关闭")
        self.button_1.setObjectName("button_1")
        self.button_1.setMaximumSize(40, 40)
        self.button_1.setMinimumSize(40, 40)
        self.button_1.setStyleSheet("#button_1{border-bottom: 1px solid rgba(231, 233, 237, 1);border-left: 0px;border-top: 0px;border-right: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-size:20px;font-family:SimHei;vertical-align: middle;}#button_1:hover{background-color: rgb(251,115,115);}")
        self.button_1.pressed.connect(self.close_win_1)
        self.hbox_1.addWidget(self.button_1, Qt.AlignRight)
        self.vbox.addLayout(self.hbox_1)

        label_3 = QLabel()
        label_3.setObjectName("label_3")
        label_3.setText("®")
        label_3.setMaximumSize(36, 31)
        label_3.setMinimumSize(36, 31)
        label_3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label_3.setStyleSheet("background-color: rgb(55,99,214,255);border: 0px;border-radius: 10px;padding: 0px;margin-left: 10px;margin-right: 5px;margin-top: 10px;width: 16px;height: 16px;font-size: 26px;font-family: Arial-BoldItalicMT, Arial;color: rgba(255,255,255,255);")
        self.hbox_2.addWidget(label_3)

        label_5 = QLabel()
        # 设置行间距
        label_5.setText("<p style='line-height:120%'>消息定时发送工具 V1.0</p>")
        # 自动换行设置
        label_5.setWordWrap(True)
        font_1 = QFont()
        # 设置字间距
        font_1.setLetterSpacing(QFont.PercentageSpacing, 108)
        label_5.setFont(font_1)
        label_5.adjustSize()
        label_5.setObjectName("label_5")
        label_5.setMaximumSize(700, 30)
        label_5.setMinimumSize(120, 30)
        label_5.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_5.setStyleSheet("#label_5{border:0px;margin-right: 0px;margin-left: 0px;margin-top: 10px;margin-bottom: 0px;padding: 0px;background-color: rgb(246,246,246);color: rgb(0,0,0);font-weight: bold;text-align: center;font-size: 14px;font-family: Microsoft YaHei;}")
        self.hbox_2.addWidget(label_5)
        self.vbox.addLayout(self.hbox_2)

        label_6 = QLabel()
        # 设置行间距
        label_6.setText("<p style='line-height:120%'>Copyright©2022-2022 Z-Tool.\nAll Rights Reserved. </p>")
        # 自动换行设置
        label_6.setWordWrap(True)
        font_1 = QFont()
        # 设置字间距
        font_1.setLetterSpacing(QFont.PercentageSpacing, 108)
        label_6.setFont(font_1)
        label_6.adjustSize()
        label_6.setObjectName("label_6")
        label_6.setMaximumSize(700, 60)
        label_6.setMinimumSize(120, 60)
        label_6.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_6.setStyleSheet("#label_6{border:0px;margin-right: 0px;margin-left: 40px;margin-top: 0px;margin-bottom: 0px;padding: 0px;background-color: rgb(246,246,246);color: rgb(0,0,0);text-align: center;font-size: 12px;font-family: Microsoft YaHei;}")
        self.vbox.addWidget(label_6)

        label_2 = QLabel()
        label_2.setObjectName("label_2")
        label_2.setMaximumSize(700, 20)
        label_2.setMinimumSize(120, 20)
        label_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_2.setStyleSheet("#label_2{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 16px;font-family: SimHei;}")
        self.vbox.addWidget(label_2)

        self.label_3 = QLabel()
        self.label_3.setMaximumSize(620, 42)
        self.label_3.setMinimumSize(120, 42)
        self.hbox_3.addWidget(self.label_3, Qt.AlignCenter | Qt.AlignVCenter)

        self.button_2 = QPushButton("确 定")
        self.button_2.setMaximumSize(81, 42)
        self.button_2.setMinimumSize(81, 42)
        self.button_2.pressed.connect(self.close_win_1)
        self.button_2.setStyleSheet("QPushButton{border-radius: 5px;border: 0px;margin-top: 12px;margin-bottom: 0px;margin-right: 16px;margin-left: 0px;padding: 0px;background-color: rgb(246,246,246);background-color: rgb(20,108,185,180);vertical-align: middle;text-align: center;font-size: 14px;font-family: SimHei;color: rgb(255,255,255);}""QPushButton:hover{background-color: rgb(5,186,251,180);}""QPushButton:pressed{background: black;border: None;}")
        self.hbox_3.addWidget(self.button_2, Qt.AlignRight)
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

    def close_win_1(self):
        """
        :title 关闭程序(槽)，判断有点问题，主窗口最小化时点击关闭弹窗窗口主窗口会显示出来
        :return: None
        """
        try:
            self.close()
            if self.ui.isMinimized() or not self.ui.isVisible():
                info("系统托盘【关于】弹窗应用在最小化或者不可见的情况下关闭弹窗！")
                self.ui.showMinimized()
                self.ui.setWindowFlags(Qt.SplashScreen)
                self.ui.show()
            else:
                info("系统托盘【关于】弹窗应用可见的情况下先关闭弹窗再设置主页面使能！")
                self.ui.stackUnder(self)
                self.ui.setEnabled(True)
                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
                self.ui.show()
        except Exception as e:
            info("关于弹窗报错，具体原因如下：")
            info(e)

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.m_flag = True
                self.m_position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        except Exception as e:
            info("鼠标按下事件报错，具体原因如下所示！")
            error(e)

    def mouseMoveEvent(self, qmouseevent):
        try:
            if Qt.LeftButton and self.m_flag:
                self.move(qmouseevent.globalPos()-self.m_position)  # 更改窗口位置
                qmouseevent.accept()
        except Exception as e:
            info("鼠标按下事件报错，具体原因如下所示！")
            error(e)

    def mouseReleaseEvent(self, qmouseevent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app1 = QApplication(argv)
    form = SystemTrayAbout("")
    form.show()
    exit(app1.exec_())
