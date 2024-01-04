#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-01-03 20:59
# @Author  : 刘航宇
# @File    : task-timer.py
# @Description :
import threading
import time


class TimerManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, interval, function):
        task = {'name': task_name, 'interval': interval, 'function': function, 'next_execution': time.time() + interval}
        self.tasks.append(task)

    def run(self):
        while True:
            current_time = time.time()

            for task in self.tasks:
                if current_time >= task['next_execution']:
                    task['function']()
                    task['next_execution'] = current_time + task['interval']

            time.sleep(1)  # 等待1秒，避免过于频繁的循环


# 示例任务函数
def task1():
    print("Task 1 executed at:", time.strftime("%Y-%m-%d %H:%M:%S"))


def task2():
    print("Task 2 executed at:", time.strftime("%Y-%m-%d %H:%M:%S"))


def main():
    while True:
        print("nihao")
        time.sleep(1)


# 创建定时器管理器
timer_manager = TimerManager()

# 添加任务到管理器
timer_manager.add_task("Task 1", 5, task1)  # 每5秒执行一次
timer_manager.add_task("Task 2", 10, task2)  # 每10秒执行一次

# 启动定时器管理器
timer_thread = threading.Thread(target=timer_manager.run)
timer_thread.start()

main()
# 主线程继续执行其他操作，定时器线程在后台执行任务
