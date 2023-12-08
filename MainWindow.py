import TempMethon as temp_methon
import EntryMethon as entry_methon
import tkinter as tk


# 定义按钮点击事件处理函数
def show_popup(tkwin):
    # 创建一个新的顶级窗口
    popup = tkwin.Toplevel(window)
    popup.title("弹窗")
    
    # 在弹窗中添加标签和按钮
    label = tkwin.Label(popup, text="这是一个弹窗")
    label.pack()
    
    button = tkwin.Button(popup, text="关闭", command=popup.destroy)
    button.pack()

def BtnRunClick(tkwin,entry_min,entry_max):
    if temp_methon.table_run(entry_min,entry_max) == False:
        show_popup(tkwin)

# 创建主窗口
window = tk.Tk()
window.title("温升实验数据分析器")
# 设置窗口大小
window.geometry("800x600")  # 设置宽度为800像素，高度为600像素

# 创建一个菜单
ChooseMenu = tk.Menu(window)

# 创建下拉菜单
dropdown_menu = tk.Menu(ChooseMenu, tearoff=0)
dropdown_menu.add_command(label="打开文件夹" , command=lambda: temp_methon.open_folder(label_current_file))
dropdown_menu.add_command(label="打开文件", command=lambda: temp_methon.open_file(label_current_file))
#dropdown_menu.add_command(label="Option 3")

# 将下拉菜单添加到菜单中
ChooseMenu.add_cascade(label="文件", menu=dropdown_menu)
# 将菜单与窗口关联
window.config(menu=ChooseMenu)

# 创建按钮和标签
#btn_open_folder = tk.Button(window, text="打开文件夹", command=temp_methon.open_folder)
#btn_open_file = tk.Button(window, text="打开文件", command=temp_methon.open_file)

label_ymin = tk.Label(window, text="Y轴最小值：")
label_ymax = tk.Label(window, text="Y轴最大值：")

# 绑定Y轴最小值输入框鼠标点击事件和焦点离开事件
entry_ymin = tk.Entry(window)
default_min = 60
entry_ymin.insert(0, default_min)
entry_ymin.config(fg='grey')
entry_ymin.bind('<FocusIn>',  lambda event: entry_methon.on_entry_click(event, entry_ymin, default_min,tk))
entry_ymin.bind('<FocusOut>',  lambda event: entry_methon.on_entry_leave(event, entry_ymin, default_min))

# 绑定Y轴最小值输入框鼠标点击事件和焦点离开事件
entry_ymax = tk.Entry(window)
default_max = 115
entry_ymax.insert(0, default_max)
entry_ymax.config(fg='grey')
entry_ymax.bind('<FocusIn>',  lambda event: entry_methon.on_entry_click(event, entry_ymax, default_max,tk))
entry_ymax.bind('<FocusOut>',  lambda event: entry_methon.on_entry_leave(event, entry_ymax, default_max))
label_current_file = tk.Label(window, text="点击\"文件\"打开需要分析的log文件")

btn_run = tk.Button(window, text="运行", command=BtnRunClick(tk,entry_ymin,entry_ymax))
# 布局按钮和标签
#btn_open_folder.pack()
#btn_open_file.pack()
label_current_file.pack(anchor='w')
label_ymin.pack(anchor='w')
entry_ymin.pack(anchor='w')
label_ymax.pack(anchor='w')
entry_ymax.pack(anchor='w')
btn_run.pack()
# 运行主窗口
window.mainloop()
