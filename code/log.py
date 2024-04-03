# qwq 已完成编辑 qwq

import datetime
from config import *

log = []  # 用来记录历史记录
level_dict = {  # 把对应到数字重要等级转化为文字等级
    0: "Information",
    1: "Warning",
    2: "Error"
}


def get_log_time():  # 获取当前时间
    return datetime.datetime.now().strftime(log_time)


def output_log(text, level=0):  # 输出日志
    print(log_format % (get_log_time(), level_dict[level], text))
    log.append(log_format % (get_log_time(), level_dict[level], text))


def save_log():
    with open("./log/%s.txt" % datetime.datetime.now().strftime("%Y%m%d%H%M%S"), "w", encoding="utf-8") as file:
        file.write("\n".join(log))


o = output_log  # 为方便调用方便调用定义一个简短名称
