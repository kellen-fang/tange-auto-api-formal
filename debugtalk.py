import datetime
import random
import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def create_phone():
    # 随机生成手机号
    second = "14444444"
    # second = "8675704759"
    # 最后4位数字
    third = ''
    code = third.join(random.choice("0123456789") for i in range(4))
    # 拼接手机号
    return "{}{}".format(second, code)


def create_email():
    # 用数字0-9 和字母a-z 生成随机邮箱。
    list_sum = [i for i in range(10)] + ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k",
                                         "l", "M", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                                         "w", "x", "y", "z"]
    start = "test-"
    middle = ""
    ending = ["@tange-ai.com"]
    for i in range(5):
        a = str(random.choice(list_sum))
        middle = middle + a
    return start + middle + random.choice(ending)

def get_last_today():
    # 获取当前时间
    now = datetime.datetime.now()
    # 获取今天零点
    zeroToday = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                         microseconds=now.microsecond)
    # 获取23:59:59
    lastToday = zeroToday + datetime.timedelta(hours=23, minutes=59, seconds=59)
    last_today = lastToday.strftime("%Y-%m-%d %H:%M:%S")
    return last_today


def get_zero_today():
    now = datetime.datetime.now()
    # 获取今天零点
    zeroToday = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                         microseconds=now.microsecond)
    zero_today = zeroToday.strftime("%Y-%m-%d %H:%M:%S")
    return zero_today


if __name__ == "__main__":
    for i in range(2):
        print(create_phone())
        print(create_email())
