#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : python_project
@File           : ButtonPopup.py
@Software       : PyCharm
@Time           : 2022/9/27 20:58
@Description    : 重写关闭应用的选择弹窗：1、最小化到系统托盘；2、直接关闭应用
"""
from os import path
from logging import info
from sys import argv, exit
from PyQt5.Qt import Qt, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, qApp, QCheckBox


class CloseButtonPopup(QWidget):
    def __init__(self, main_win, parent=None):
        super(CloseButtonPopup, self).__init__(parent)
        self.file_path = path.dirname(path.abspath(__file__))
        self.full_path = self.file_path.replace("\\", "/")
        self.ui = main_win
        self.setWindowTitle("系统提示")
        # 设置ICO
        self.setWindowIcon(QIcon('%s/pic/main.png' % self.full_path))
        # 设置对象名称
        self.setObjectName("MainWindow1")
        self.width = 320
        self.height = 200
        self.resize(self.width, self.height)
        self.setStyleSheet("#MainWindow1{border: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);}")
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
        label_0.setObjectName("label_0")
        label_0.setMaximumSize(24, 50)
        label_0.setMinimumSize(24, 50)
        label_0.setStyleSheet("#label_0{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);}")
        self.hbox_1.addWidget(label_0)

        label_1 = QLabel("系统提示")
        label_1.setObjectName("label_1")
        label_1.setMaximumSize(700, 50)
        label_1.setMinimumSize(120, 50)
        label_1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_1.setStyleSheet("#label_1{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 16px;font-family: SimHei;}")
        self.hbox_1.addWidget(label_1)

        self.button_1 = QPushButton()
        self.button_1.setText("×")
        self.button_1.setToolTip("关闭")
        self.button_1.setObjectName("button_1")
        self.button_1.setMaximumSize(50, 50)
        self.button_1.setMinimumSize(50, 50)
        self.button_1.setStyleSheet("#button_1{border-bottom: 1px solid rgba(231, 233, 237, 1);border-left: 0px;border-top: 0px;border-right: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-size:20px;font-family:SimHei;vertical-align: middle;}#button_1:hover{background-color: rgb(251,115,115);}")
        self.button_1.pressed.connect(self.close_win)
        self.hbox_1.addWidget(self.button_1, Qt.AlignRight)
        self.vbox.addLayout(self.hbox_1)

        self.rbutton_1 = QRadioButton("最小化到系统托盘")
        self.rbutton_1.setMaximumSize(400, 38)
        self.rbutton_1.setMinimumSize(400, 38)
        self.rbutton_1.setChecked(True)
        self.rbutton_1.setStyleSheet("border: 0px;margin-left: 24px;margin-top: 18px;margin-right: 0px;margin-bottom: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgba(89, 99, 109, 1);text-align: center;font-size: 14px;font-family: SimHei;")
        self.vbox.addWidget(self.rbutton_1, Qt.AlignCenter | Qt.AlignVCenter)

        self.rbutton_2 = QRadioButton("直接关闭应用")
        self.rbutton_2.setMaximumSize(400, 34)
        self.rbutton_2.setMinimumSize(400, 34)
        self.rbutton_2.setStyleSheet("border: 0px;margin-left: 24px;margin-top: 12px;background-color: rgb(246,246,246);font-weight: bold;color: rgba(89, 99, 109, 1);text-align: center;font-size: 14px;font-family: SimHei;")
        self.vbox.addWidget(self.rbutton_2, Qt.AlignCenter | Qt.AlignVCenter)

        label_2 = QLabel()
        label_2.setObjectName("label_2")
        label_2.setMaximumSize(700, 40)
        label_2.setMinimumSize(120, 40)
        label_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label_2.setStyleSheet("#label_2{border-bottom: 1px solid rgba(231, 233, 237, 1);border-right: 0px;border-left: 0px;border-top: 0px;margin: 0px;padding: 0px;background-color: rgb(246,246,246);font-weight: bold;color: rgb(0,0,0);text-align: center;font-size: 16px;font-family: SimHei;}")
        self.vbox.addWidget(label_2)

        self.checkbox_1 = QCheckBox("不再提示！")
        self.checkbox_1.setMaximumSize(620, 42)
        self.checkbox_1.setMinimumSize(120, 42)
        self.checkbox_1.setObjectName("checkbox_1")
        self.checkbox_1.setStyleSheet("#checkbox_1{border: 0px;margin-left: 20px;margin-right: 0px;margin-top: 10px;margin-bottom: 0px;padding: 0px;background-color: rgb(20,108,185,0);vertical-align: middle;text-align: center;color: rgba(0,0,0);text-align: center;font-size: 12px;font-family: SimHei;}")
        self.hbox_2.addWidget(self.checkbox_1, Qt.AlignCenter | Qt.AlignVCenter)
        self.button_2 = QPushButton("确 定")
        self.button_2.setMaximumSize(81, 42)
        self.button_2.setMinimumSize(81, 42)
        self.button_2.pressed.connect(self.select_method)
        self.button_2.setStyleSheet("QPushButton{border-radius: 5px;border: 0px;margin-top: 12px;margin-bottom: 0px;margin-right: 16px;margin-left: 0px;padding: 0px;background-color: rgb(246,246,246);background-color: rgb(20,108,185,180);vertical-align: middle;text-align: center;font-size: 14px;font-family: SimHei;color: rgb(255,255,255);}""QPushButton:hover{background-color: rgb(5,186,251,180);}""QPushButton:pressed{background: black;border: None;}")
        self.hbox_2.addWidget(self.button_2, Qt.AlignRight)
        self.vbox.addLayout(self.hbox_2)

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
        info("系统提示弹窗关闭！")
        self.checkbox_1.setChecked(False)
        self.close()
        self.ui.setEnabled(True)
        self.ui.showNormal()
        self.ui.activateWindow()
        self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.ui.show()

    def minimize(self):
        """
        :title 最小化窗口
        :return: None
        """
        self.close()
        self.ui.showMinimized()
        self.ui.setWindowFlags(Qt.SplashScreen)
        self.ui.show()
        self.ui.setEnabled(True)

    def exit_win(self):
        """
        :title 关闭整个应用
        :return: None
        """
        self.close()
        self.ui.setVisible(False)
        qApp.quit()

    def select_method(self):
        """
        :title 判断选择的是：最小化到系统托盘，还是：直接关闭应用，再进行处理
        :return: None
        """
        if self.rbutton_1.isChecked():
            info("经选择后最小化应用！")
            self.minimize()
        else:
            info("经选择后关闭整个应用！")
            self.exit_win()


if __name__ == "__main__":
    app1 = QApplication(argv)
    form = CloseButtonPopup("")
    form.show()
    exit(app1.exec_())
