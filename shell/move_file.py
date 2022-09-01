# coding:utf-8
import datetime
import os
import platform


# 备份原文件
def file_backup(filename):
    if os.path.exists(filename):
        now_date = datetime.datetime.now()
        os.rename(filename, filename + str(datetime.datetime.strftime(now_date, UsePlatform())))
    else:
        print(filename + "不存在")


def UsePlatform():
    system_name = platform.system()
    if system_name == "Windows":
        print("Call Windows tasks")
        return '%Y-%m-%d-%H-%M-%S'
    elif system_name == "Linux":
        print("Call Linux tasks")
        return '%Y-%m-%d-%H:%M:%S'
    else:
        print("Other System tasks")
        return '%Y-%m-%d-%H:%M:%S'


# 重命名
def rename(old_file_name, new_file_name):
    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)
    else:
        print(old_file_name + "不存在")


if __name__ == '__main__':
    # rename("test123.txt", "test123_bak.txt")
    file_backup("test123.txt")
