import os
import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

folder_path=""
Open_file_path=""

def open_folder():
    global folder_path
    global Open_file_path
    folder_path = filedialog.askdirectory()
    Open_file_path=""
    # 打开文件夹的逻辑处理

def open_file():
    global folder_path
    global Open_file_path
    Open_file_path = filedialog.askopenfilename()
    folder_path=""
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
        if "soc_monitor" not in file_name:
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

def table_run():
    global folder_path
    global Open_file_path
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
    if Open_file_path:
        file_table_run(Open_file_path,ymin,ymax)

# 创建主窗口
window = tk.Tk()
# 设置窗口大小
window.geometry("800x600")  # 设置宽度为800像素，高度为600像素

# 创建按钮和标签
btn_open_folder = tk.Button(window, text="打开文件夹", command=open_folder)
btn_open_file = tk.Button(window, text="打开文件", command=open_file)
btn_run = tk.Button(window, text="运行", command=table_run)
label_ymin = tk.Label(window, text="Y轴最小值：")
label_ymax = tk.Label(window, text="Y轴最大值：")
entry_ymin = tk.Entry(window)
entry_ymax = tk.Entry(window)
entry_current_file = tk.Entry(window)

# 布局按钮和标签
btn_open_folder.pack()
btn_open_file.pack()
entry_current_file.pack()
label_ymin.pack()
entry_ymin.pack()
label_ymax.pack()
entry_ymax.pack()
btn_run.pack()
# 运行主窗口
window.mainloop()
