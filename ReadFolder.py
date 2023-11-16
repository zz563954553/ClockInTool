#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : python_project
@File           : ReadFolder.py
@Software       : PyCharm
@Time           : 2022-09-16 16:07
@Description    : 用于读取文件
"""
from os import walk, path
from logging import info
from time import localtime


class ReadFolder(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.root_path = list()
        self.dirs_name = list()
        self.files_name = list()

    def get_all_files_names(self):
        """
        :title 获取目标文件夹下所有的文件名，文件夹及其路径
        :return: None
        """
        for root, dirs, files in walk(self.folder_path):
            self.root_path.append(root)
            self.dirs_name.append(dirs)
            self.files_name.append(files)

    def get_files_modify_time(self):
        """
        :title 把目标文件夹下所有的文件名，文件夹及其路径分别放到不同的列表中再集中return
        :return: [file_names, modify_time, files_path]，file_names：所有文件名，modify_time：所有文件对应的更新时间，files_path：所有文件对应的完整路径
        """
        modify_time = list()
        file_names = list()
        files_path = list()
        self.get_all_files_names()
        if len(self.root_path) != 0:
            for i in range(0, len(self.files_name)):
                if len(self.files_name[i]) != 0:
                    for j in range(0, len(self.files_name[i])):
                        full_file_path = self.root_path[i] + "\\%s" % self.files_name[i][j]
                        files_path.append(full_file_path)
                        transition_var = localtime(path.getmtime(full_file_path))
                        year_var = str(transition_var[0])
                        month_var = str(transition_var[1])
                        day_var = str(transition_var[2])
                        hour_var = str(transition_var[3])
                        minute_var = str(transition_var[4])
                        second_var = str(transition_var[5])
                        month_var = month_var.rjust(2, "0")
                        day_var = day_var.rjust(2, "0")
                        hour_var = hour_var.rjust(2, "0")
                        minute_var = minute_var.rjust(2, "0")
                        second_var = second_var.rjust(2, "0")
                        time_var = year_var+"/"+month_var+"/"+day_var+" "+hour_var+":"+minute_var+":"+second_var
                        modify_time.append(time_var)
                        if self.files_name[i][j] not in file_names:
                            file_names.append(self.files_name[i][j])
                        else:
                            file_names = file_names
                else:
                    pass
            if len(file_names) != len(files_path):
                info("存在不同文件夹下有相同文件名的情况，请务必保证各个文件名都不相同！返回二维空列表！")
                return [[], [], []]
            else:
                info("已返回正确的二维列表！")
                return [file_names, modify_time, files_path]
        else:
            info("root路径列表为空，返回二维空列表！")
            return [[], [], []]


if __name__ == '__main__':
    t = ReadFolder(r"E:\zhouzhi\auto\helpothers\yuanxiao\5")
    tt = t.get_files_modify_time()
    for n in range(0, len(tt)):
        print(len(tt[n]))
        print(tt[n])

