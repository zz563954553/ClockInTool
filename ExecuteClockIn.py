#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : HaoKao
@File           : ExecuteClockIn.py
@Software       : PyCharm
@Time           : 2023-08-30 11:24
@Description    : 定时发送消息线程
"""
from os import path
from time import sleep, strftime
from logging import info, error
from PyQt5.QtCore import QThread
from schedule import every, run_pending
from pywinauto import Application, mouse, keyboard


class ExecuteClockIn(QThread):
    def __init__(self, app_name, app_path, dialog_name, interval_time, task_time, send_content, task_type):
        super(ExecuteClockIn, self).__init__()
        self.app_name = app_name
        self.app_path = app_path
        self.dialog_name = dialog_name
        self.interval_time = interval_time
        self.task_time = task_time
        self.send_content = send_content
        self.task_type = task_type

    def wxwork_clockin(self):
        """
        :title 企业微信自动发送消息
        :return: None
        """
        try:
            Application(backend='uia').start(self.app_path)
            sleep(3)
            app = Application(backend='uia').connect(title='企业微信')
            wind_calc = app['企业微信']
            coordinate = wind_calc.rectangle()
            l_coordinate = coordinate.left
            b_coordinate = coordinate.bottom
            mouse.click(coords=(l_coordinate + 25, b_coordinate - 560))
            sleep(0.5)
            mouse.click(coords=(l_coordinate + 180, b_coordinate - 610))
            sleep(0.5)
            keyboard.send_keys(self.dialog_name)
            sleep(0.5)
            keyboard.send_keys("{ENTER}")
            mouse.click(coords=(l_coordinate + 600, b_coordinate - 90))
            sleep(0.5)
            keyboard.send_keys(self.send_content)
            keyboard.send_keys("{ENTER}")
        except Exception as e:
            info("执行企业微信自动发送消息报错！")
            error(e)

    def wechat_clockin(self):
        """
        :title 微信自动发送消息
        :return: None
        """
        try:
            Application(backend='uia').start(self.app_path)
            sleep(3)
            app = Application(backend='uia').connect(title='微信')
            wx_win = app.window(class_name='WeChatMainWndForPC')
            # wx_win.print_control_identifiers(depth=None, filename=None)
            wx_search_box = wx_win.child_window(title="搜索", control_type="Edit")
            wx_search_box.click_input()
            wx_search_box.type_keys(self.dialog_name)
            sleep(1)
            keyboard.send_keys('{ENTER}')
            sleep(3)
            keyboard.send_keys(self.send_content)
            sleep(1)
            keyboard.send_keys('{ENTER}')
        except Exception as e:
            info("执行微信自动发送消息报错！")
            error(e)

    def wechat_fixed_num_automatic_reply(self):
        """
        :title 微信固定人数自动回复消息
        :return: None
        """
        try:
            recorded_data = dict()
            group_name = list()
            data_time_var_1 = strftime("%Y-%m-%d %H:%M:%S")
            Application(backend='uia').start(self.app_path)
            sleep(3)
            app = Application(backend='uia').connect(title='微信')
            wx_win = app.window(class_name='WeChatMainWndForPC')
            # 过滤掉群、订阅号、服务通知之类的消息
            filter_info_data_file = r"%s\data\DialogueList.txt" % path.dirname(path.abspath(__file__))
            with open(filter_info_data_file, "r+", encoding="utf-8") as f:
                data = f.readlines()
            for name_num in range(len(data)):
                group_name.append(data[name_num].split("\n")[0])
            # 获取微信排在第一位窗口的对话名称
            all_conversation_windows = wx_win.child_window(title="会话", control_type="List")
            while True:
                try:
                    first_window_all_sub_elements_1 = all_conversation_windows.children()
                    for i in range(len(group_name)):
                        window_num = 0
                        info("当前联系人是：%s" % group_name[i])
                        for j in range(len(first_window_all_sub_elements_1)):
                            if "条新消息" in first_window_all_sub_elements_1[window_num].window_text():
                                last_first_window = wx_win.child_window(title=first_window_all_sub_elements_1[window_num].window_text(), control_type="ListItem")
                                last_first_window.click_input()
                            elif first_window_all_sub_elements_1[window_num].window_text() == group_name[i]:
                                last_first_window = wx_win.child_window(title=group_name[i], control_type="ListItem")
                                last_first_window.click_input()
                                msg_control = last_first_window.descendants(control_type="Text")
                                if recorded_data.get(group_name[i]) is None:
                                    last_time = msg_control[-2].texts()[-1]
                                    last_msg = msg_control[-1].texts()[-1]
                                    recorded_data[group_name[i]] = [last_time, last_msg]
                                    info("[%s] 联系人【%s】的last_time:%s" % (data_time_var_1, group_name[i], last_time))
                                    info("[%s] 联系人【%s】的last_msg:%s" % (data_time_var_1, group_name[i], last_msg))
                                else:
                                    old_time = recorded_data[group_name[i]][0]
                                    old_msg = recorded_data[group_name[i]][1]
                                    last_time = msg_control[-2].texts()[-1]
                                    last_msg = msg_control[-1].texts()[-1]
                                    if old_time == last_time and old_msg == last_msg:
                                        info("联系人【%s】当前没有新消息，无需自动回复！" % group_name[i])
                                    elif last_msg == self.send_content:
                                        recorded_data[group_name[i]] = [last_time, last_msg]
                                    else:
                                        recorded_data[group_name[i]] = [last_time, last_msg]
                                        sleep(1)
                                        keyboard.send_keys(self.send_content)
                                        sleep(1)
                                        keyboard.send_keys('{ENTER}')
                                        sleep(1)
                                break
                            elif j == len(first_window_all_sub_elements_1) - 1 and first_window_all_sub_elements_1[window_num].window_text() != group_name[i]:
                                info("没有符合条件的个人聊天窗口！")
                                last_time = ""
                                last_msg = ""
                                recorded_data[group_name[i]] = [last_time, last_msg]
                                info("[%s] 联系人【%s】的last_time:%s" % (data_time_var_1, group_name[i], last_time))
                                info("[%s] 联系人【%s】的last_msg:%s" % (data_time_var_1, group_name[i], last_msg))
                                break
                            else:
                                window_num += 1
                        info(recorded_data)
                except Exception as e:
                    info("新消息出现后第一次定位控件/控件被手动删除报错！报错内容如下所示！")
                    error(e)
        except Exception as e:
            info("执行微信固定自动回复消息报错！")
            error(e)

    def wechat_batch_automatic_reply(self):
        """
        :title 微信批量自动回复消息
        :return: None
        """
        try:
            window_num = 0
            window_names = list()
            group_name = list()
            data_time_var_1 = strftime("%Y-%m-%d %H:%M:%S")
            Application(backend='uia').start(self.app_path)
            sleep(3)
            app = Application(backend='uia').connect(title='微信')
            wx_win = app.window(class_name='WeChatMainWndForPC')
            # 过滤掉群、订阅号、服务通知之类的消息
            filter_info_data_file = r"%s\data\FilteringInformation.txt" % path.dirname(path.abspath(__file__))
            with open(filter_info_data_file, "r+", encoding="utf-8") as f:
                data = f.readlines()
            for name_num in range(len(data)):
                group_name.append(data[name_num].split("\n")[0])
            # 获取微信排在第一位窗口的对话名称
            all_conversation_windows = wx_win.child_window(title="会话", control_type="List")
            first_window_all_sub_elements_1 = all_conversation_windows.children()
            last_first_window_name = first_window_all_sub_elements_1[window_num].window_text()
            window_names.append(last_first_window_name)
            while True:
                for i in range(len(group_name)):
                    if group_name[i] in last_first_window_name:
                        window_num += 1
                        break
                    else:
                        continue
                if window_num < len(first_window_all_sub_elements_1):
                    last_first_window_name = first_window_all_sub_elements_1[window_num].window_text()
                    window_names.append(last_first_window_name)
                else:
                    break
                if window_names[-1] == window_names[-2]:
                    break
            if window_num != len(first_window_all_sub_elements_1):
                last_first_window_name_1 = first_window_all_sub_elements_1[window_num].window_text()
                last_first_window = wx_win.child_window(title=last_first_window_name_1, control_type="ListItem")
                last_first_window.click_input()
                msg_control = last_first_window.descendants(control_type="Text")
                last_time = msg_control[-2].texts()[-1]
                last_msg = msg_control[-1].texts()[-1]
                info("[%s] last_time:%s" % (data_time_var_1, last_time))
                info("[%s] last_msg:%s" % (data_time_var_1, last_msg))
            else:
                info("没有符合条件的个人聊天窗口！")
                last_time = ""
                last_msg = ""
                last_first_window_name_1 = ""
                info("[%s] last_time:%s" % (data_time_var_1, last_time))
                info("[%s] last_msg:%s" % (data_time_var_1, last_msg))
            while True:
                window_num_1 = 0
                window_names_2 = list()
                data_time_var_2 = strftime("%Y-%m-%d %H:%M:%S")
                # # 获取微信排在第一位窗口的对话名称
                # all_conversation_windows = wx_win.child_window(title="会话", control_type="List")
                first_window_all_sub_elements_2 = all_conversation_windows.children()
                new_first_window_name = first_window_all_sub_elements_2[window_num_1].window_text()
                window_names_2.append(new_first_window_name)
                while True:
                    for i in range(len(group_name)):
                        if group_name[i] in new_first_window_name:
                            window_num_1 += 1
                            break
                        else:
                            continue
                    if window_num_1 < len(first_window_all_sub_elements_2):
                        new_first_window_name = first_window_all_sub_elements_2[window_num_1].window_text()
                        window_names_2.append(new_first_window_name)
                    else:
                        break
                    if window_names_2[-1] == window_names_2[-2]:
                        break
                if window_num_1 != len(first_window_all_sub_elements_2):
                    new_first_window_name_1 = first_window_all_sub_elements_2[window_num_1].window_text()
                    new_first_window = wx_win.child_window(title=new_first_window_name_1, control_type="ListItem")
                    new_first_window.click_input()
                    sleep(1)
                    try:
                        msg_control = new_first_window.descendants(control_type="Text")
                        new_time = msg_control[-2].texts()[-1]
                        new_msg = msg_control[-1].texts()[-1]
                        info("[%s] new_time:%s" % (data_time_var_2, new_time))
                        info("[%s] new_msg:%s" % (data_time_var_2, new_msg))
                        if new_first_window_name_1 == last_first_window_name_1:
                            if new_time == last_time and new_msg == last_msg:
                                info("[%s] 没有新消息！" % data_time_var_2)
                            elif new_msg == self.send_content:
                                info("[%s] 没有新消息！" % data_time_var_2)
                                last_time = new_time
                                last_msg = new_msg
                                info("[%s] last_time:%s" % (data_time_var_2, last_time))
                                info("[%s] last_msg:%s" % (data_time_var_2, last_msg))
                            else:
                                sleep(1)
                                keyboard.send_keys(self.send_content)
                                sleep(1)
                                keyboard.send_keys('{ENTER}')
                                sleep(1)
                                last_time = new_time
                                last_msg = new_msg
                                info("[%s] last_time:%s" % (data_time_var_2, last_time))
                                info("[%s] last_msg:%s" % (data_time_var_2, last_msg))
                        else:
                            sleep(1)
                            keyboard.send_keys(self.send_content)
                            sleep(1)
                            keyboard.send_keys('{ENTER}')
                            sleep(1)
                            last_first_window_name_1 = new_first_window_name_1
                            last_time = new_time
                            last_msg = new_msg
                            info("[%s] last_time:%s" % (data_time_var_2, last_time))
                            info("[%s] last_msg:%s" % (data_time_var_2, last_msg))
                    except Exception as e:
                        info("新消息出现后第一次定位控件/控件被手动删除报错！报错内容如下所示！")
                        error(e)
                        break
                else:
                    info("没有符合条件的个人聊天窗口！")
                    new_time = ""
                    new_msg = ""
                    info("[%s] new_time:%s" % (data_time_var_1, new_time))
                    info("[%s] new_msg:%s" % (data_time_var_1, new_msg))
        except Exception as e:
            info("执行微信自动回复消息报错！")
            error(e)

    def tim_clockin(self):
        """
        :title TIM自动发送消息
        :return: None
        """
        try:
            Application(backend='uia').start(self.app_path)
            sleep(3)
            app = Application(backend='uia').connect(title='TIM')
            wx_win = app.window(class_name='TXGuiFoundation')
            # wx_win.print_control_identifiers(depth=None, filename=None)
            wx_search_box = wx_win.child_window(title="搜索", control_type="Edit")
            wx_search_box.click_input()
            wx_search_box.type_keys(self.dialog_name)
            sleep(1)
            keyboard.send_keys('{ENTER}')
            sleep(3)
            keyboard.send_keys(self.send_content)
            sleep(1)
            keyboard.send_keys('{ENTER}')
        except Exception as e:
            info("执行TIM自动发送消息报错！")
            error(e)

    def run(self):
        """
        :title 重写run，判断应用程序再发送消息
        :return: None
        """
        if self.task_type == "执行任务":
            mouth_second = 0
            if self.app_name == "企业微信":
                task = self.wxwork_clockin
            elif self.app_name == "微信":
                task = self.wechat_clockin
            else:
                task = self.wxwork_clockin
            if self.interval_time == "每分钟":
                every().minute.at(":%s" % self.task_time.split(":")[-1]).do(task)
            elif self.interval_time == "每小时":
                every().hour.do(task)
            elif self.interval_time == "每天":
                every().day.at(self.task_time[0:5]).do(task)
            elif self.interval_time == "每周一":
                every().monday.at(self.task_time[0:5]).do(task)
            elif self.interval_time == "每周二":
                every().wednesday.at(self.task_time[0:5]).do(task)
            elif self.interval_time == "每周三":
                every().wednesday.at(self.task_time[0:5]).do(task)
            elif self.interval_time == "每周四":
                every().wednesday.at(self.task_time[0:5]).do(task)
            elif self.interval_time == "每周五":
                every().wednesday.at(self.task_time[0:5]).do(task)
            elif self.interval_time == "每周六":
                every().wednesday.at(self.task_time[0:5]).do(task)
            else:
                every().wednesday.at(self.task_time[0:5]).do(task)
            while True:
                mouth_second += 1
                run_pending()
                if mouth_second == 2592000:
                    info("一个月时间限制已到，任务自动停止！")
                    break
                else:
                    if mouth_second % 3600 == 0:
                        info("已执行%s小时！" % int(mouth_second / 3600))
                    else:
                        pass
                sleep(1)
        elif self.task_type == "批量自动回复":
            while True:
                self.wechat_batch_automatic_reply()
        else:
            while True:
                self.wechat_fixed_num_automatic_reply()


if __name__ == "__main__":
    from LogGeneration import display_and_save_logs
    log_dir_path = r"%s\log\ClockInTool.log" % path.dirname(path.abspath(__file__))
    display_and_save_logs(log_dir_path)
    try:
        eci = ExecuteClockIn("企业微信", r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe", "周志", "每分钟", "08:00:00", "早上好", "自动回复")
        eci.wechat_fixed_num_automatic_reply()
    except Exception as er:
        print(er)
