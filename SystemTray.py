#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : python_project
@File           : SystemTray.py
@Software       : PyCharm
@Time           : 2022-09-27 9:51
@Description    : 重写应用在Windows系统托盘右下角的一些使用方法
"""
from os import path
from logging import info
from PyQt5.QtCore import Qt, QUrl
from SystemTrayExit import SystemTrayExit
from SystemTrayAbout import SystemTrayAbout
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon


class TrayIcon(QSystemTrayIcon):
    def __init__(self, mainwindow, pic_path, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.setToolTip("消息定时发送工具")
        self.full_path = pic_path
        self.menu = QMenu()
        self.showaction1 = QAction(QIcon('%s/pic/start.png' % self.full_path), "启动", self)
        self.showaction2 = QAction(QIcon('%s/pic/about.png' % self.full_path), "关于", self)
        self.showaction3 = QAction(QIcon('%s/pic/log.png' % self.full_path), "日志", self)
        self.quitaction = QAction(QIcon('%s/pic/exit.png' % self.full_path), "退出", self)
        self.icon = self.MessageIcon()
        self.setIcon(QIcon("%s/pic/main.png" % self.full_path))
        self.ui = mainwindow
        self.app_about = SystemTrayAbout(self.ui)
        self.app_exit = SystemTrayExit(self.ui)
        self.ui.setWindowFlags(Qt.FramelessWindowHint)
        self.createmenu()

    def createmenu(self):
        """
        :title 添加鼠标右键显示的菜单栏，以及菜单栏绑定对应的逻辑函数
        :return: None
        """
        self.menu.addAction(self.showaction1)
        self.menu.addAction(self.showaction2)
        self.menu.addAction(self.showaction3)
        self.menu.addAction(self.quitaction)
        self.setContextMenu(self.menu)
        self.showaction1.triggered.connect(self.show_window)
        self.showaction2.triggered.connect(self.showabout)
        self.showaction3.triggered.connect(self.showlog)
        self.quitaction.triggered.connect(self.quit)
        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.oniconclicked)

    @staticmethod
    def showlog():
        """
        :title 打开日志文件
        :return: None
        """
        try:
            url = QUrl.fromLocalFile(r"%s\log\ClockInTool.log" % path.dirname(path.abspath(__file__)))
            QDesktopServices.openUrl(url)
        except Exception as e:
            info("打开日志文件失败！失败原因如下所示！")
            info(e)

    def showabout(self):
        """
        :title 展示版权
        :return: None
        """
        try:
            self.app_about.show()
            if self.ui.isMinimized() or not self.ui.isVisible():
                pass
            else:
                self.app_about.move(int(self.ui.pos().x() + (self.ui.width - self.app_about.width) / 2), int(self.ui.pos().y() + (self.ui.height - self.app_about.height) / 2))
                self.ui.setEnabled(False)
        except Exception as e:
            info(e)

    def show_window(self):
        """
        :title 菜单栏中启动的逻辑函数，若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        :return: None
        """
        info("点击系统托盘的【启动】，正常显示主页面！")
        self.ui.showNormal()
        self.ui.activateWindow()
        self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.ui.show()

    def quit(self):
        """
        :title 菜单栏中退出的逻辑函数
        :return: None
        """
        info("点击系统托盘的【退出】，弹出确认退出窗口！")
        try:
            self.app_exit.show()
            if self.ui.isMinimized() or not self.ui.isVisible():
                pass
            else:
                self.app_exit.move(int(self.ui.pos().x() + (self.ui.width - self.app_exit.width) / 2), int(self.ui.pos().y() + (self.ui.height - self.app_exit.height) / 2))
                self.ui.setEnabled(False)
        except Exception as e:
            info(e)

    def oniconclicked(self, reason):
        """
        :title 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        :param reason:点击icon所传递的信号
        :return: None
        """
        if reason == 2 or reason == 3:
            self.showMessage("RPA", "点击退出", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                info("点击系统托盘图标，主界面不可见，则显示正常窗口大小！")
                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
                self.ui.show()
            else:
                info("点击系统托盘图标，主界面可见，则显示窗口最小化！")
                # 若不是最小化，则最小化
                self.ui.showMinimized()
                self.ui.setWindowFlags(Qt.SplashScreen)
                self.ui.show()
