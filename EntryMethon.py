
# 定义鼠标点击事件处理函数
def on_entry_click(event,entry,default_value,tk):
    if entry.get() == str(default_value):
        entry.delete(0, tk.END)
        entry.config(fg='black')

# 定义焦点离开事件处理函数
def on_entry_leave(event,entry,default_value):
    if entry.get() == '':
        entry.insert(0, default_value)
        entry.config(fg='grey')