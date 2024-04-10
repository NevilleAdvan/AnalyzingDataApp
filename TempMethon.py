import os
import re
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox

folder_path=""
Open_file_path=""

def open_folder(result_label):
    global folder_path
    global Open_file_path
    folder_path = filedialog.askdirectory()
    Open_file_path=""
    result_label.config(text="当前打开文件夹: ["+ folder_path + "] ")
    # 打开文件夹的逻辑处理

def open_file(result_label):
    global folder_path
    global Open_file_path
    Open_file_path = filedialog.askopenfilename()
    folder_path=""
    result_label.config(text="当前打开文件: ["+ Open_file_path + "] ")
    # 打开文件的逻辑处理
    

def file_table_run(file_path,ymin , ymax):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # 存储温度数据的列表
        temperature_list = []
        # 提取温度数据
        for line in lines:
            # 使用正则表达式匹配温度数据
            match = re.search(r'\|(\d+\.\d+)', line)
            if match:
                temperature = float(match.group(1))
                temperature_list.append(temperature)


        #print(temperature_list)
        # 绘制折线图
        plt.figure(1)
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定使用微软雅黑字体
        plt.plot(range(len(temperature_list)), temperature_list)
        plt.xlabel('时间')
        plt.ylabel('温度')
        plt.ylim(ymin , ymax)
        max_temperature = max(temperature_list)
        title= file_path + "-温度折线图-" +  str(max_temperature) + "°"
        plt.title(title)
        # 显示图形
        plt.show()

    

def folder_table_run(set_folder_path,ymin,ymax):
    # 获取文件夹中的所有文件
    file_list = os.listdir(set_folder_path)
    tablenum = 1

    # 遍历文件列表
    for file_name in file_list:
        if ".log" not in file_name:
            continue
        # 构建文件路径
        file_path = os.path.join(set_folder_path, file_name)
        print(file_path)
        # 存储温度数据的列表
        temperature_list = []
        # 读取文件数据
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # 提取温度数据
            for line in lines:
                # 使用正则表达式匹配温度数据
                match = re.search(r'\|(\d+\.\d+)', line)
                if match:
                    temperature = float(match.group(1))
                    temperature_list.append(temperature)


        #print(temperature_list)
        # 绘制折线图
        plt.figure(tablenum)
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定使用微软雅黑字体
        plt.plot(range(len(temperature_list)), temperature_list)
        plt.xlabel('时间')
        plt.ylabel('温度')
        plt.ylim(ymin , ymax)
        max_temperature = max(temperature_list)
        title= file_name + "-温度折线图-" +  str(max_temperature) + "°"
        plt.title(title)
        tablenum = tablenum+1
    # 显示图形
    plt.show()

def table_run(entry_ymin,entry_ymax):
    global folder_path
    global Open_file_path
    ret = False
    if entry_ymin.get() == "":
        print("entry_ymin is empty，set default ymix is 60")
        ymin = 60
    else:
        ymin = float(entry_ymin.get())
    print("Valid ymin:", ymin)

    if entry_ymax.get() == "":
        print("entry_ymax is empty，set default ymax is 115")
        ymax = 115
    else:
        ymax = float(entry_ymax.get())
    print(ymax)
    if folder_path:
        folder_table_run(folder_path,ymin,ymax)
        ret= True
    elif Open_file_path:
        file_table_run(Open_file_path,ymin,ymax)
        ret= True
    print("Valid ret:", ret)
    return ret

