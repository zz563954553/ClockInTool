#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : HaoKao
@File           : ClockInTool.py
@Software       : PyCharm
@Time           : 2023-08-30 14:18
@Description    : 定时发送消息UI工具
"""
from os import path
from time import strftime
from PyQt5.QtCore import QSize
from logging import info, error
from CommonHelper import read_qss
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtGui import QIcon, QMovie
from configparser import ConfigParser
from CloseButtonPopup import CloseButtonPopup
from LogGeneration import display_and_save_logs
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QGroupBox, QTextBrowser, QLabel, QComboBox, QPushButton, QSpacerItem, QSizePolicy, QTextEdit, QApplication, QFileDialog, QLineEdit, QTimeEdit
try:
    from ExecuteClockIn import ExecuteClockIn
except Exception as e:
    info("导入执行脚本报错！")
    error(e)


class ClockInTool(QWidget):
    def __init__(self, parent=None):
        super(ClockInTool, self).__init__(parent)
        log_dir_path = r"%s\log\ClockInTool.log" % path.dirname(path.abspath(__file__))
        display_and_save_logs(log_dir_path)
        self.ini_file_path = r"%s\data\initdata.ini" % path.dirname(path.abspath(__file__))
        self.setObjectName("Form")
        self.setWindowTitle("消息定时发送工具")
        self.setWindowIcon(QIcon(r"%s\icon\main.png" % path.dirname(path.abspath(__file__))))
        # 获取显示器分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.width = 791
        self.height = 627
        self.resize(self.width, self.height)
        # 鼠标事件参数初始化
        self._right_rect = None
        self._bottom_rect = None
        self._corner_rect = None
        self._move_drag = None
        self.move_DragPosition = None
        # 设置鼠标跟踪
        self.setMouseTracking(True)
        # 界面部件初始化
        self.verticalLayout_0 = None
        self.horizontalLayout_0 = None
        self.right_half_0 = None
        self.left_half_0 = None
        self.button_0_1 = None
        self.button_0_2 = None
        self.label_0_1 = QLabel()
        self.gridLayout_3 = None
        self.verticalLayout_3 = None
        self.horizontalLayout_4 = None
        self.groupBox_2 = None
        self.gridLayout_4 = None
        self.textBrowser = None
        self.groupBox = None
        self.gridLayout = None
        self.horizontalLayout_2 = None
        self.label_2 = None
        self.comboBoxBaudrate = None
        self.horizontalLayout = None
        self.label = None
        self.comboBoxSerialPort = None
        self.horizontalLayout_3 = None
        self.label_3 = None
        self.btnOpenClose = None
        self.upBtnClear = None
        self.gridLayout_2 = None
        self.groupBox_3 = None
        self.horizontalLayout_5 = None
        self.textEdit = None
        self.verticalLayout = None
        self.btnSend = None
        self.btnClear = None
        self.serial = None
        self.groupBox_2 = None
        self.horizontalLayout_6 = None
        self.label_4 = None
        self.receiveBtnClear = None
        self.label_5 = None
        self.horizontalLayout_7 = None
        self.rec_BtnClear = None
        self.select_time = None
        self.horizontalLayout_8 = None
        self.label_6 = None
        self.horizontalLayout_9 = None
        self.label_7 = None
        self.execute_button = None
        self.horizontalLayout_10 = None
        self.label_8 = None
        self.automatic_reply_button = None
        self.horizontalLayout_11 = None
        self.label_9 = None
        self.fix_automatic_reply_button = None
        # 初始化线程
        self.ec = None
        self.ec_1 = None
        self.ec_2 = None
        self.ec_3 = None
        # 初始化应用路径
        self.wechat_path = ""
        self.wxwork_path = ""
        self.tim_path = ""
        # 初始化事件过滤器
        self.label_0_1.installEventFilter(self)
        # 应用路径初始化
        self.select_file_path = ""
        # 界面初始化
        self.setup_ui()
        self.read_qss()
        # 初始化关闭弹窗
        self.one = CloseButtonPopup(self)

    def setup_ui(self):
        """
        :title 初始化界面
        :return: None
        """
        # 先读取数据
        ini_data = self.read_ini_data()
        app_name = ini_data[0]
        app_path = ini_data[1]
        dialog_name = ini_data[2]
        interval_time = ini_data[3]
        task_time = ini_data[4]
        send_content = ini_data[5]
        # 竖向布局
        self.verticalLayout_0 = QVBoxLayout()
        self.verticalLayout_0.setObjectName("verticalLayout_3")
        self.verticalLayout_0.setSpacing(0)
        self.verticalLayout_0.setContentsMargins(0, 0, 0, 0)
        # 横向布局
        self.horizontalLayout_0 = QHBoxLayout()
        self.horizontalLayout_0.setObjectName("horizontalLayout_4")
        self.horizontalLayout_0.setSpacing(0)
        self.horizontalLayout_0.setContentsMargins(0, 0, 0, 0)

        self.right_half_0 = QWidget()
        self.right_half_0.setObjectName("topRight")
        self.right_half_0.setMinimumSize(150, 40)
        self.right_half_0.setMaximumSize(self.screenwidth, 40)
        self.left_half_0 = QWidget()
        self.left_half_0.setObjectName("topLeft")
        self.left_half_0.setMinimumSize(120, 40)
        self.left_half_0.setMaximumSize(self.screenwidth, 40)
        self.horizontalLayout_0.addWidget(self.right_half_0, 96)
        self.horizontalLayout_0.addWidget(self.left_half_0, 4)

        # 顶端左半部分图片采用栅格布局
        layout3_1 = QGridLayout()
        layout3_1.setSpacing(0)
        layout3_1.setContentsMargins(0, 0, 0, 0)
        self.right_half_0.setLayout(layout3_1)
        layout3_0 = QHBoxLayout()
        layout3_0.setSpacing(10)
        layout3_0.setContentsMargins(0, 0, 0, 0)
        label_3_0 = QLabel()
        label_3_0.setText("®")
        label_3_0.setObjectName("copyrightGraphic")
        label_3_0.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        label_3_0.setMaximumSize(31, 21)
        label_3_0.setMinimumSize(31, 21)
        layout3_0.addWidget(label_3_0, Qt.AlignCenter | Qt.AlignVCenter)
        layout3_1.addLayout(layout3_0, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_0_1.setText("定时消息发送工具")
        self.label_0_1.setObjectName("appName")
        self.label_0_1.setMaximumSize(self.screenwidth, 40)
        self.label_0_1.setMinimumSize(120, 40)
        self.label_0_1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout3_0.addWidget(self.label_0_1, Qt.AlignCenter | Qt.AlignVCenter)
        # 顶端右半部分采用水平布局
        layout_0_2 = QHBoxLayout()
        layout_0_2.setContentsMargins(0, 0, 0, 0)
        layout_0_2.setSpacing(0)
        self.left_half_0.setLayout(layout_0_2)
        # 测试动态gif图
        label_0_0 = QLabel()
        label_0_0.setFixedSize(40, 40)
        gif = QMovie(r"%s\pic\test.gif" % path.dirname(path.abspath(__file__)))
        label_0_0.setMovie(gif)
        gif.start()
        layout_0_2.addWidget(label_0_0, Qt.AlignCenter | Qt.AlignVCenter)

        # 设置最小化按钮
        self.button_0_1 = QPushButton()
        self.button_0_1.setText("－")
        self.button_0_1.setToolTip("最小化")
        self.button_0_1.setMaximumSize(40, 40)
        self.button_0_1.setMinimumSize(40, 40)
        self.button_0_1.setObjectName("minButton")
        layout_0_2.addWidget(self.button_0_1, Qt.AlignCenter | Qt.AlignVCenter)
        self.button_0_1.clicked.connect(self.showMinimized)
        # 设置关闭按钮
        self.button_0_2 = QPushButton()
        self.button_0_2.setText("×")
        self.button_0_2.setToolTip("关闭")
        self.button_0_2.setMaximumSize(40, 40)
        self.button_0_2.setMinimumSize(40, 40)
        self.button_0_2.setObjectName("closeButton")
        layout_0_2.addWidget(self.button_0_2, Qt.AlignCenter | Qt.AlignVCenter)
        self.button_0_2.clicked.connect(self.select_btn)

        # 栅栏布局
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        # 竖向布局
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        # 横向布局
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        # 虚线框1
        self.groupBox_2 = QGroupBox()
        self.groupBox_2.setObjectName("groupBox")
        self.groupBox_2.setTitle("操作消息")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # 输入框
        operating_instructions = """★★★操作步骤：
    1、先选择需要发送消息的应用（TIM功能未完善）；
    2、再选择对应应用的启动路径（文件的完整路径）；
    3、输入对应应用聊天框的名称（完整名称）；
    4、选择需要执行的时间间隔；
    5、修改需要执行的具体时间；
    6、点击执行任务按钮即会按照上述设置执行任务。
★★★注意事项：
    1、应用已经正常登录的情况下；
    2、操作应用名称和应用路径一定要对应；
    3、聊天框的名称要完全正确；
    4、只有点击执行任务按钮才会保存当前设置的信息，
    5、只有微信才有自动回复功能，但是需要提前设置过滤群组信息，
    6、微信的执行任务和自动回复最好只开启其中一个功能。
"""
        self.textBrowser = QTextEdit(self.groupBox_2)
        self.textBrowser.setObjectName("QTextEdit")
        self.textBrowser.setPlaceholderText(operating_instructions)
        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        # 虚线框2
        self.groupBox = QGroupBox()
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("操作配置")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        # 横向布局
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # 标签1
        self.label_2 = QLabel()
        self.label_2.setFixedSize(100, 25)
        self.label_2.setObjectName("label")
        self.label_2.setText("应用路径：")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.label_2)
        # 下拉框
        self.comboBoxBaudrate = QPushButton(self.groupBox)
        self.comboBoxBaudrate.setObjectName("selectBtn")
        self.comboBoxBaudrate.setFixedSize(150, 25)
        self.comboBoxBaudrate.setText("请选择文件")
        try:
            if app_path != "":
                self.select_file_path = app_path
                self.comboBoxBaudrate.setText(self.select_file_path.split("/")[-1])
                self.comboBoxBaudrate.setToolTip(self.select_file_path)
        except Exception as init_data_path_e:
            info("初始化数据中应用程序路径有问题！")
            error(init_data_path_e)
        self.comboBoxBaudrate.clicked.connect(self.select_file)
        self.horizontalLayout_2.addWidget(self.comboBoxBaudrate)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        # 横向布局
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 标签2
        self.label = QLabel()
        self.label.setFixedSize(100, 25)
        self.label.setObjectName("label")
        self.label.setText("操作应用：")
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label)
        # 应用选择下拉框
        self.comboBoxSerialPort = QComboBox(self.groupBox)
        self.comboBoxSerialPort.setObjectName("comboBox")
        self.comboBoxSerialPort.setFixedSize(150, 25)
        self.comboBoxSerialPort.setEditable(True)
        self.comboBoxSerialPort.lineEdit().setAlignment(Qt.AlignCenter)
        app_items = ["企业微信", "微信", "TIM"]
        self.comboBoxSerialPort.addItems(app_items)
        try:
            if app_name != "":
                index = app_items.index(app_name)
                self.comboBoxSerialPort.setCurrentIndex(index)
        except Exception as init_data_name_e:
            info("初始化数据中应用程序名称有问题！")
            error(init_data_name_e)
        self.comboBoxSerialPort.currentTextChanged.connect(self.app_change)
        self.horizontalLayout.addWidget(self.comboBoxSerialPort)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        # 横向布局
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        # 标签3
        self.label_3 = QLabel()
        self.label_3.setFixedSize(100, 25)
        self.label_3.setObjectName("label")
        self.label_3.setText("聊天名称：")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3.addWidget(self.label_3)
        # 打开串口按钮
        self.btnOpenClose = QLineEdit()
        self.btnOpenClose.setObjectName("lineEdit")
        self.btnOpenClose.setFixedSize(150, 25)
        self.btnOpenClose.setPlaceholderText("请输入对话名称")
        if dialog_name != "":
            self.btnOpenClose.setText(dialog_name)
        self.btnOpenClose.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3.addWidget(self.btnOpenClose)

        # 横向布局
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        # 标签4
        self.label_4 = QLabel()
        self.label_4.setFixedSize(100, 25)
        self.label_4.setObjectName("label")
        self.label_4.setText("间隔周期：")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_6.addWidget(self.label_4)
        # 接收标志按钮
        self.receiveBtnClear = QComboBox(self.groupBox)
        self.receiveBtnClear.setObjectName("comboBox")
        self.receiveBtnClear.setFixedSize(150, 25)
        self.receiveBtnClear.setEditable(True)
        self.receiveBtnClear.lineEdit().setAlignment(Qt.AlignCenter)
        interval_time_items = ["每分钟", "每小时", "每天", "每周一", "每周二", "每周三", "每周四", "每周五", "每周六", "每周日"]
        self.receiveBtnClear.addItems(interval_time_items)
        try:
            if interval_time != "":
                index = interval_time_items.index(interval_time)
                self.receiveBtnClear.setCurrentIndex(index)
        except Exception as init_data_time_e:
            info("初始化数据中间隔时间有问题！")
            error(init_data_time_e)
        self.horizontalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_6.addWidget(self.receiveBtnClear)

        # 横向布局
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_4")
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        # 标签5
        self.label_5 = QLabel()
        self.label_5.setFixedSize(100, 25)
        self.label_5.setObjectName("label")
        self.label_5.setText("发送时间：")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_7.addWidget(self.label_5)
        # 清空按钮
        self.select_time = QTimeEdit(QTime.currentTime(), self)
        self.select_time.setDisplayFormat('HH:mm:ss')
        self.select_time.lineEdit().setAlignment(Qt.AlignCenter)
        self.select_time.setFixedSize(150, 25)
        self.select_time.setObjectName("lineEdit")
        try:
            if task_time != "":
                qtime = QTime.fromString(task_time, "hh:mm:ss")
                self.select_time.setTime(qtime)
        except Exception as init_data_e:
            info("初始化数据中发送时间有问题！")
            error(init_data_e)
        self.horizontalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_7.addWidget(self.select_time)

        # 横向布局
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_4")
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        # 标签5
        self.label_6 = QLabel()
        self.label_6.setFixedSize(100, 25)
        self.label_6.setObjectName("label")
        self.label_6.setText("清空操作：")
        self.label_6.setAlignment(Qt.AlignCenter)
        # 清空按钮
        self.upBtnClear = QPushButton(self.groupBox)
        self.upBtnClear.setObjectName("btn")
        self.upBtnClear.setFixedSize(150, 25)
        self.upBtnClear.setText("清空内容")
        self.upBtnClear.clicked.connect(self.up_btn_clear_click)
        self.horizontalLayout_8.addWidget(self.label_6)
        self.horizontalLayout_8.addWidget(self.upBtnClear)

        # 横向布局
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_4")
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        # 标签5
        self.label_7 = QLabel()
        self.label_7.setFixedSize(100, 25)
        self.label_7.setObjectName("label")
        self.label_7.setText("任务操作：")
        self.label_7.setAlignment(Qt.AlignCenter)
        # 清空按钮
        self.execute_button = QPushButton(self.groupBox)
        self.execute_button.setObjectName("btn")
        self.execute_button.setFixedSize(150, 25)
        self.execute_button.setText("执行任务")
        self.execute_button.clicked.connect(self.perform_task)
        self.horizontalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_9.addWidget(self.execute_button)

        # 横向布局
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_4")
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_10, 7, 0, 1, 1)
        # 标签8
        self.label_8 = QLabel()
        self.label_8.setFixedSize(100, 25)
        self.label_8.setObjectName("label")
        self.label_8.setText("批量设置：")
        self.label_8.setAlignment(Qt.AlignCenter)
        # 批量自动回复按钮
        self.automatic_reply_button = QPushButton(self.groupBox)
        self.automatic_reply_button.setObjectName("btn")
        self.automatic_reply_button.setFixedSize(150, 25)
        self.automatic_reply_button.setText("批量自动回复")
        self.automatic_reply_button.clicked.connect(self.auto_reply_task)
        self.horizontalLayout_10.addWidget(self.label_8)
        self.horizontalLayout_10.addWidget(self.automatic_reply_button)
        if self.comboBoxSerialPort.currentText() == "微信":
            self.label_8.setVisible(True)
            self.automatic_reply_button.setVisible(True)
        else:
            self.label_8.setVisible(False)
            self.automatic_reply_button.setVisible(False)

        # 横向布局
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_4")
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_11, 8, 0, 1, 1)
        # 标签8
        self.label_9 = QLabel()
        self.label_9.setFixedSize(100, 25)
        self.label_9.setObjectName("label")
        self.label_9.setText("固定设置：")
        self.label_9.setAlignment(Qt.AlignCenter)
        # 批量自动回复按钮
        self.fix_automatic_reply_button = QPushButton(self.groupBox)
        self.fix_automatic_reply_button.setObjectName("btn")
        self.fix_automatic_reply_button.setFixedSize(150, 25)
        self.fix_automatic_reply_button.setText("固定自动回复")
        self.fix_automatic_reply_button.clicked.connect(self.auto_fix_reply_task)
        self.horizontalLayout_11.addWidget(self.label_9)
        self.horizontalLayout_11.addWidget(self.fix_automatic_reply_button)
        if self.comboBoxSerialPort.currentText() == "微信":
            self.label_9.setVisible(True)
            self.fix_automatic_reply_button.setVisible(True)
        else:
            self.label_9.setVisible(False)
            self.fix_automatic_reply_button.setVisible(False)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacer_item, 9, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        # 虚线框
        self.groupBox_3 = QGroupBox()
        self.groupBox_3.setObjectName("groupBox")
        self.groupBox_3.setTitle("发送消息")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # 横向布局
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        # 输入框
        self.textEdit = QTextEdit()
        self.textEdit.setObjectName("textEdit")
        if send_content != "":
            self.textEdit.setText(send_content)
        self.horizontalLayout_5.addWidget(self.textEdit)
        # 竖向布局
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # 发送按钮
        self.btnSend = QPushButton()
        self.btnSend.setMinimumSize(QSize(0, 50))
        self.btnSend.setObjectName("btn")
        self.btnSend.setText("发送测试")
        self.btnSend.clicked.connect(self.send_test)
        self.verticalLayout.addWidget(self.btnSend)
        # 清空按钮
        self.btnClear = QPushButton()
        self.btnClear.setMinimumSize(QSize(0, 50))
        self.btnClear.setObjectName("btn")
        self.btnClear.setText("清空内容")
        self.btnClear.clicked.connect(self.btn_clear_click)

        self.verticalLayout.addWidget(self.btnClear)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 2)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_0.addLayout(self.horizontalLayout_0)
        self.verticalLayout_0.addLayout(self.gridLayout_3)
        self.setLayout(self.verticalLayout_0)
        self.textBrowser.setLineWrapMode(QTextBrowser.LineWrapMode.WidgetWidth)

    def read_ini_data(self):
        """
        :title 读取初始化数据
        :return: 以列表的形式返回ini文件的数据
        """
        conf = ConfigParser()
        conf.read(self.ini_file_path, encoding="gbk")
        app_name = conf.get("initdata", "app_name")
        app_path = conf.get("initdata", "app_path")
        dialog_name = conf.get("initdata", "dialog_name")
        interval_time = conf.get("initdata", "interval_time")
        task_time = conf.get("initdata", "task_time")
        send_content = conf.get("initdata", "send_content")
        self.wechat_path = conf.get("apps_path", "wechat_path")
        self.wxwork_path = conf.get("apps_path", "wxwork_path")
        self.tim_path = conf.get("apps_path", "tim_path")
        ini_data = [app_name, app_path, dialog_name, interval_time, task_time, send_content, self.wechat_path, self.wxwork_path, self.tim_path]
        info("读取到的初始文件数据：%s" % ini_data)
        return ini_data

    def edit_ini_data(self, app_name, app_path, dialog_name, interval_time, task_time, send_content):
        """
        :title 读取初始化数据
        :return: 以列表的形式返回ini文件的数据
        """
        try:
            conf = ConfigParser()
            conf.read(self.ini_file_path, encoding="gbk")
            conf.set('initdata', 'app_name', app_name)
            conf.set('initdata', 'app_path', app_path)
            conf.set('initdata', 'dialog_name', dialog_name)
            conf.set('initdata', 'interval_time', interval_time)
            conf.set('initdata', 'task_time', task_time)
            conf.set('initdata', 'send_content', send_content)
            write_content = [app_name, app_path, dialog_name, interval_time, task_time, send_content]
            info("配置信息重新写入的内容为：%s" % write_content)
            with open(self.ini_file_path, 'w') as f:
                conf.write(f)
        except Exception as edit_ini_data_e:
            info("配置信息重新写入报错！")
            error(edit_ini_data_e)

    def auto_reply_task(self):
        """
        :title 开始执行微信自动回复任务
        :return: None
        """
        data_time_var = strftime("%Y-%m-%d %H:%M:%S")
        try:
            from ExecuteClockIn import ExecuteClockIn
            if self.automatic_reply_button.text() == "批量自动回复":
                self.automatic_reply_button.setText("停止批量回复")
                app_name = self.comboBoxSerialPort.currentText()
                app_path = self.select_file_path
                dialog_name = self.btnOpenClose.text()
                interval_time = self.receiveBtnClear.currentText()
                task_time = self.select_time.text()
                send_content = self.textEdit.toPlainText()
                task_type = "批量自动回复"
                if app_path == "":
                    info("应用路径不能为空！")
                    self.textBrowser.insertPlainText("【%s】 应用路径不能为空！\n" % data_time_var)
                elif dialog_name == "":
                    info("对话名称不能为空！")
                    self.textBrowser.insertPlainText("【%s】 对话名称不能为空！\n" % data_time_var)
                elif send_content == "":
                    info("发送内容不能为空！")
                    self.textBrowser.insertPlainText("【%s】 发送内容不能为空！\n" % data_time_var)
                else:
                    self.textBrowser.insertPlainText("【%s】 已开启批量自动回复！\n" % data_time_var)
                    info("已开启批量自动回复！")
                    self.ec_1 = ExecuteClockIn(app_name, app_path, dialog_name, interval_time, task_time, send_content, task_type)
                    self.ec_1.start()
            else:
                if self.ec_1:
                    self.ec_1.terminate()
                self.automatic_reply_button.setText("批量自动回复")
                info("已终止批量自动回复！")
                self.textBrowser.insertPlainText("【%s】 已停止批量自动回复任务！\n" % data_time_var)
        except Exception as auto_reply_e:
            info("批量自动回复功能报错，原因如下所示！")
            error(auto_reply_e)
            self.textBrowser.insertPlainText("【%s】 批量自动回复功能报错，原因如下所示！\n" % data_time_var)
            self.textBrowser.insertPlainText("【%s】 %s\n" % (data_time_var, e))

    def auto_fix_reply_task(self):
        """
        :title 开始执行微信自动回复任务
        :return: None
        """
        data_time_var = strftime("%Y-%m-%d %H:%M:%S")
        try:
            from ExecuteClockIn import ExecuteClockIn
            if self.fix_automatic_reply_button.text() == "固定自动回复":
                self.fix_automatic_reply_button.setText("停止固定回复")
                app_name = self.comboBoxSerialPort.currentText()
                app_path = self.select_file_path
                dialog_name = self.btnOpenClose.text()
                interval_time = self.receiveBtnClear.currentText()
                task_time = self.select_time.text()
                send_content = self.textEdit.toPlainText()
                task_type = "固定自动回复"
                if app_path == "":
                    info("应用路径不能为空！")
                    self.textBrowser.insertPlainText("【%s】 应用路径不能为空！\n" % data_time_var)
                elif dialog_name == "":
                    info("对话名称不能为空！")
                    self.textBrowser.insertPlainText("【%s】 对话名称不能为空！\n" % data_time_var)
                elif send_content == "":
                    info("发送内容不能为空！")
                    self.textBrowser.insertPlainText("【%s】 发送内容不能为空！\n" % data_time_var)
                else:
                    self.textBrowser.insertPlainText("【%s】 已开启固定自动回复！\n" % data_time_var)
                    info("已开启固定自动回复！")
                    self.ec_3 = ExecuteClockIn(app_name, app_path, dialog_name, interval_time, task_time, send_content, task_type)
                    self.ec_3.start()
            else:
                if self.ec_3:
                    self.ec_3.terminate()
                self.fix_automatic_reply_button.setText("固定自动回复")
                info("已终止固定自动回复！")
                self.textBrowser.insertPlainText("【%s】 已停止固定自动回复任务！\n" % data_time_var)
        except Exception as auto_reply_e:
            info("固定自动回复功能报错，原因如下所示！")
            error(auto_reply_e)
            self.textBrowser.insertPlainText("【%s】 固定自动回复功能报错，原因如下所示！\n" % data_time_var)
            self.textBrowser.insertPlainText("【%s】 %s\n" % (data_time_var, e))

    def app_change(self):
        """
        :title 选择的是微信则显示自动回复按钮和标签，否则不显示
        :return: None
        """
        if self.comboBoxSerialPort.currentText() == "微信":
            self.label_8.setVisible(True)
            self.automatic_reply_button.setVisible(True)
            self.label_9.setVisible(True)
            self.fix_automatic_reply_button.setVisible(True)
            try:
                if self.wechat_path != "":
                    self.select_file_path = self.wechat_path
                    self.comboBoxBaudrate.setText(self.select_file_path.split("/")[-1])
                    self.comboBoxBaudrate.setToolTip(self.select_file_path)
            except Exception as init_data_path_e:
                info("初始化数据中微信程序路径有问题！")
                error(init_data_path_e)
        elif self.comboBoxSerialPort.currentText() == "企业微信":
            self.label_8.setVisible(False)
            self.automatic_reply_button.setVisible(False)
            self.label_9.setVisible(False)
            self.fix_automatic_reply_button.setVisible(False)
            try:
                if self.wxwork_path != "":
                    self.select_file_path = self.wxwork_path
                    self.comboBoxBaudrate.setText(self.select_file_path.split("/")[-1])
                    self.comboBoxBaudrate.setToolTip(self.select_file_path)
            except Exception as init_data_path_e:
                info("初始化数据中企业微信程序路径有问题！")
                error(init_data_path_e)
        else:
            self.label_8.setVisible(False)
            self.automatic_reply_button.setVisible(False)
            self.label_9.setVisible(False)
            self.fix_automatic_reply_button.setVisible(False)
            try:
                if self.tim_path != "":
                    self.select_file_path = self.tim_path
                    self.comboBoxBaudrate.setText(self.select_file_path.split("/")[-1])
                    self.comboBoxBaudrate.setToolTip(self.select_file_path)
            except Exception as init_data_path_e:
                info("初始化数据中TIM程序路径有问题！")
                error(init_data_path_e)

    def perform_task(self):
        """
        :title 开始执行测试任务
        :return: None
        """
        data_time_var = strftime("%Y-%m-%d %H:%M:%S")
        try:
            from ExecuteClockIn import ExecuteClockIn
            try:
                if self.execute_button.text() == "执行任务":
                    self.execute_button.setText("停止任务")
                    app_name = self.comboBoxSerialPort.currentText()
                    app_path = self.select_file_path
                    dialog_name = self.btnOpenClose.text()
                    interval_time = self.receiveBtnClear.currentText()
                    task_time = self.select_time.text()
                    send_content = self.textEdit.toPlainText()
                    task_type = "执行任务"
                    if app_path == "":
                        info("应用路径不能为空！")
                        self.textBrowser.insertPlainText("【%s】 应用路径不能为空！\n" % data_time_var)
                    elif dialog_name == "":
                        info("对话名称不能为空！")
                        self.textBrowser.insertPlainText("【%s】 对话名称不能为空！\n" % data_time_var)
                    elif send_content == "":
                        info("发送内容不能为空！")
                        self.textBrowser.insertPlainText("【%s】 发送内容不能为空！\n" % data_time_var)
                    else:
                        self.edit_ini_data(app_name, app_path, dialog_name, interval_time, task_time, send_content)
                        self.textBrowser.insertPlainText("【%s】 应用名称：%s\n" % (data_time_var, app_name))
                        self.textBrowser.insertPlainText("【%s】 应用路径：%s\n" % (data_time_var, app_path))
                        self.textBrowser.insertPlainText("【%s】 对话名称：%s\n" % (data_time_var, dialog_name))
                        self.textBrowser.insertPlainText("【%s】 间隔时间：%s\n" % (data_time_var, interval_time))
                        self.textBrowser.insertPlainText("【%s】 执行时间：%s\n" % (data_time_var, task_time))
                        self.textBrowser.insertPlainText("【%s】 发送内容：%s\n" % (data_time_var, send_content))
                        info("应用名称：%s,应用路径：%s,对话名称：%s,间隔时间：%s,执行时间：%s,发送内容：%s。" % (app_name, app_path, dialog_name, interval_time, task_time, send_content))
                        info("开始执行任务！")
                        self.textBrowser.insertPlainText("【%s】 开始执行任务！\n" % data_time_var)
                        self.ec = ExecuteClockIn(app_name, app_path, dialog_name, interval_time, task_time, send_content, task_type)
                        self.ec.start()
                else:
                    if self.ec:
                        self.ec.terminate()
                    self.execute_button.setText("执行任务")
                    info("已经停止任务！")
                    self.textBrowser.insertPlainText("【%s】 已经停止任务！\n" % data_time_var)
            except Exception as perform_task_e:
                print(perform_task_e)
        except Exception as import_e:
            info("导入执行脚本报错！")
            error(import_e)
            self.textBrowser.insertPlainText("【%s】 导入ExecuteClockIn失败：%s\n" % (data_time_var, import_e))

    def send_test(self):
        """
        :title 测试运行按钮，执行运行一次
        :return: None
        """
        data_time_var = strftime("%Y-%m-%d %H:%M:%S")
        try:
            from ExecuteClockIn import ExecuteClockIn
            try:
                app_name = self.comboBoxSerialPort.currentText()
                app_path = self.select_file_path
                dialog_name = self.btnOpenClose.text()
                interval_time = self.receiveBtnClear.currentText()
                task_time = self.select_time.text()
                send_content = self.textEdit.toPlainText()
                task_type = "执行任务"
                if app_path == "":
                    info("应用路径不能为空！")
                    self.textBrowser.insertPlainText("【%s】 应用路径不能为空！\n" % data_time_var)
                elif dialog_name == "":
                    info("对话名称不能为空！")
                    self.textBrowser.insertPlainText("【%s】 对话名称不能为空！\n" % data_time_var)
                elif send_content == "":
                    info("发送内容不能为空！")
                    self.textBrowser.insertPlainText("【%s】 发送内容不能为空！\n" % data_time_var)
                else:
                    self.textBrowser.insertPlainText("【%s】 应用名称：%s\n" % (data_time_var, app_name))
                    self.textBrowser.insertPlainText("【%s】 应用路径：%s\n" % (data_time_var, app_path))
                    self.textBrowser.insertPlainText("【%s】 对话名称：%s\n" % (data_time_var, dialog_name))
                    self.textBrowser.insertPlainText("【%s】 间隔时间：%s\n" % (data_time_var, interval_time))
                    self.textBrowser.insertPlainText("【%s】 执行时间：%s\n" % (data_time_var, task_time))
                    self.textBrowser.insertPlainText("【%s】 发送内容：%s\n" % (data_time_var, send_content))
                    info("应用名称：%s,应用路径：%s,对话名称：%s,间隔时间：%s,执行时间：%s,发送内容：%s。" % (app_name, app_path, dialog_name, interval_time, task_time, send_content))
                    info("开始测试运行！")
                    self.textBrowser.insertPlainText("【%s】 开始测试运行！\n" % data_time_var)
                    self.ec_2 = ExecuteClockIn(app_name, app_path, dialog_name, interval_time, task_time, send_content, task_type)
                    if app_name == "企业微信":
                        self.ec_2.wxwork_clockin()
                    elif app_name == "微信":
                        self.ec_2.wechat_clockin()
                    else:
                        self.ec_2.tim_clockin()
            except Exception as send_test_e:
                info("测试运行失败！")
                error(send_test_e)
                self.textBrowser.insertPlainText("【%s】 测试运行失败：%s\n" % (data_time_var, e))
        except Exception as import_e:
            info("导入执行脚本报错！")
            error(import_e)
            self.textBrowser.insertPlainText("【%s】 导入ExecuteClockIn失败：%s\n" % (data_time_var, import_e))

    def select_btn(self):
        """
        :title 确认选择弹窗，先禁用主窗口，再通过自写控件CloseButtonPopup的方法重新使能主窗口
        :return: None
        """
        self.setEnabled(False)
        if self.one.checkbox_1.isChecked() and self.one.rbutton_1.isChecked():
            self.one.select_method()
        elif self.one.checkbox_1.isChecked() and self.one.rbutton_2.isChecked():
            self.one.exit_win()
        else:
            self.one.show()
            # 使自写控件CloseButtonPopup显示在应用的中间
            x = int(self.pos().x())
            y = int(self.pos().y())
            if x == 0 and y == 0:
                self.one.move(int((self.screenwidth - self.one.width) / 2), int((self.screenheight - self.one.height) / 2))
            else:
                self.one.move(int(x + (self.width - self.one.width) / 2), int(y + (self.height - self.one.height) / 2))

    def read_qss(self):
        """
        :title 读取qss样式文件并加载所有样式，样式文件与html的css文件语法基本一致
        :return: None
        """
        style_file = r"%s\qss\MainPage.qss" % path.dirname(path.abspath(__file__))
        qss_style = read_qss(style_file)
        self.setStyleSheet(qss_style)

    def select_file(self):
        """
        :title 打开通过系统窗口选中的文件
        :return: None
        """
        data_time_var = strftime("%Y-%m-%d %H:%M:%S")
        try:
            filename = QFileDialog.getOpenFileName(self, "选取文件", "C:")
            self.select_file_path = filename[0]
            self.comboBoxBaudrate.setText(self.select_file_path.split("/")[-1])
            self.comboBoxBaudrate.setToolTip(self.select_file_path)
            info("选择的应用程序是：%s!" % self.select_file_path)
        except Exception as select_file_e:
            info("读取应用路径失败！")
            error(select_file_e)
            self.textBrowser.insertPlainText("【%s】 读取应用路径失败：%s\n" % (data_time_var, e))

    def up_btn_clear_click(self):
        """
        :title 点击清空按钮，清空发送展示信息区域内容
        :return: None
        """
        self.textBrowser.clear()
        info("已经清空接收区域信息！")

    def btn_clear_click(self):
        """
        :title 点击清空按钮，清空发送展示信息区域内容
        :return: None
        """
        self.textEdit.clear()
        info("已经清空发送区域信息！")

    def eventFilter(self, obj, event):
        """
        :title 事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式
        :param obj:对象
        :param event:鼠标事件
        :return: None
        """
        try:
            return super(ClockInTool, self).eventFilter(obj, event)
        except Exception as event_filter_e:
            info("事件过滤器报错，具体原因如下所示！")
            error(event_filter_e)

    def mousePressEvent(self, event):
        """
        :title 重写鼠标点击的事件
        :param event:鼠标点击事件
        :return: None
        """
        try:
            self.setMouseTracking(True)
            if (event.button() == Qt.LeftButton) and (event.y() < self.label_0_1.height()):
                # 鼠标左键点击标题栏区域
                self._move_drag = True
                self.setCursor(Qt.SizeAllCursor)
                self.move_DragPosition = event.globalPos() - self.pos()
                event.accept()
        except Exception as mouse_press_event_e:
            info("鼠标释放事件报错，具体原因如下所示！")
            error(mouse_press_event_e)

    def mouseMoveEvent(self, qmouseevent):
        """
        :title 重写鼠标移动事件
        :param qmouseevent: 鼠标事件
        :return: None
        """
        try:
            if Qt.LeftButton and self._move_drag:
                # 标题栏拖放窗口位置
                self.move(qmouseevent.globalPos() - self.move_DragPosition)
                qmouseevent.accept()
        except Exception as mouse_move_event_e:
            info("鼠标移动事件报错，具体原因如下所示！")
            error(mouse_move_event_e)

    def mouseReleaseEvent(self, qmouseevent):
        """
        :title 重写鼠标释放事件，鼠标释放后，各扳机复位，并恢复箭头鼠标样式
        :param qmouseevent: 鼠标事件
        :return: None
        """
        self._move_drag = False
        self.setCursor(Qt.ArrowCursor)


if __name__ == '__main__':
    from sys import argv, exit
    from SystemTray import TrayIcon

    app = QApplication(argv)
    ui = ClockInTool()
    pic_path = path.dirname(path.abspath(__file__))
    tray = TrayIcon(ui, pic_path)
    tray.show()
    tray.show_window()
    exit(app.exec_())
