from tkinter import *
def sys_callbak():
	pass
def fun_callbak():
	pass
def no_thing(event):
	popmenu.post(event.x_root,event.y_root)
window = Tk()
window.title('新闻自动抓取')
menubar = Menu(window)
help_menu = Menu(menubar,tearoff=False)
help_menu.add_command(label='添加',command=sys_callbak)
help_menu.add_command(label='修改',command=sys_callbak)
help_menu.add_separator()
help_menu.add_command(label='退出',command=sys_callbak)
menubar.add_cascade(label='系统',menu=help_menu)
funmenu = Menu(menubar)
funmenu.add_command(label='添加',command=fun_callbak)
funmenu.add_command(label='修改',command=fun_callbak)
menubar.add_cascade(label='功能',menu=funmenu)
popmenu = Menu(window)
popmenu.add_command(label='未设置',command=no_thing)
popmenu.add_command(label='想的美',command=no_thing)
frame = Frame(window,width=312,height=512)
frame.bind('<Button-3>',no_thing)
frame.grid()
window.grid()
window.config(menu=menubar)
mainloop()

from tkinter import *
 
root = Tk()
 
def create():
    top = Toplevel()
    top.title('Python')
 
    msg = Message(top, text='I love study')
    msg.pack()
 
Button(root, text='创建顶级窗口', command=create).pack()
 
mainloop()

# from tkinter import *

# root = Tk()

# root.title('Toplevel')

# Label(root, text='主顶层（默认）').pack(pady = 10)

# t1 = Toplevel(root)

# Label(t1, text='子顶层').pack(padx=10, pady=10)

# t2 = Toplevel(root)

# Label(t2, text='临时顶层').pack(padx=10, pady=10)

# t2.transient(root)

# t3 = Toplevel(root, borderwidth=5, bg='green')

# Label(t3, text='不被视窗管理的顶层控件', bg='blue', fg='white').pack(padx=10, pady=10)

# t3.overrideredirect(1)

# t3.geometry('300x100+150+150')

# root.mainloop()