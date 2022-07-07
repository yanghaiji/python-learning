# coding:utf-8
import os
import subprocess
import unicodedata


# 获取pid
def get_pid(name):
    child = subprocess.Popen(['pgrep', '-f', name], stdout=subprocess.PIPE, shell=False)
    response = child.communicate()[0]
    print(name + " 进程pid :" + response)
    return response


# 杀掉进程
def kill(pid):
    os.system("kill -9 {}".format(pid))
    print("服务已经被停止...")


# 清理日志
def remove_log(fileName):
    if os.path.exists(filename):
        os.remove(filename)
    print("日志清理完成...")


# 启动服务
def start(name):
    os.system(
        'java  -jar -Xms512m -Xmx1024m  ' + name +
        ' --spring.profiles.active=dev  > log.log 2>&1 &')
    print("服务已经启动...")


# 判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


if __name__ == '__main__':
    servername = "demo.jar"
    filename = '/log.log'
    pid = get_pid(servername)
    if is_number(pid):
        print('服务存活...' + str(pid))
        kill(pid)
        print("服务kill...")
    else:
        print("服务不存在，需要重启服务...")
    remove_log(filename)
    start(servername)
