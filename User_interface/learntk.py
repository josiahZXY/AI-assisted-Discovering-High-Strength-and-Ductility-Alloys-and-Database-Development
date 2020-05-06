#--------------------------------------
#menubar的使用方法
# import sys
# import tkinter as tk
# window=tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# l=tk.Label(window,text='',bg='yellow')
# l.pack()
# counter=0
# def do_job():
	# global counter
	# l.config(text='do'+str(counter))
	# counter+=1	
# menubar=tk.Menu(window)
# filemenu=tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='File',menu=filemenu)
# filemenu.add_command(label='New',command=do_job)
# filemenu.add_command(label='Open',command=do_job)
# filemenu.add_command(label='Save',command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='Exit',command=window.quit())
# editmenu=tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label='Cut',command=do_job)
# editmenu.add_command(label='Copy',command=do_job)
# editmenu.add_command(label='Paste',command=do_job)
# submenu=tk.Menu(filemenu,tearoff=0)
# filemenu.add_cascade(label='Import',menu=submenu,underline=0)
# submenu.add_command(label='Submenul1',command=do_job)
# window.config(menu=menubar)#把window参数改变变成menubar
# window.mainloop()
#-----------------------------------------------
#frame框架用法
# import sys
# import tkinter as tk
# window=tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# tk.Label(window,text='on the window')
# frm=tk.Frame(window)
# frm.pack()
# frm_l=tk.Frame(frm)
# frm_r=tk.Frame(frm)
# frm_l.pack(side='left')
# frm_r.pack(side='right')
# tk.Label(frm_l,text='on the frm_l1').pack()
# tk.Label(frm_l,text='on the frm_l2').pack()
# tk.Label(frm_r,text='on the frm_r1').pack()


# l=tk.Label(window,text='',bg='yellow')
# l.pack()
# window.mainloop()
#--------------------------------------------------
#messagebox
# import tkinter.messagebox 
# import tkinter as tk
# window=tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# def hit_me():
	#tk.messagebox.showinfo(title='Hi', message='hahahaha')
	#tk.messagebox.showwarning(title='Hi', message='nononono')
	#tk.messagebox.showerror(title='Hi', message='never')
	#tk.messagebox.askquestion(title='Hi', message='never') #return yes or nononono
	#tk.messagebox.askyesno(title='Hi', message='never')#return True,False
	#tk.messagebox.askretrycancel(title='Hi', message='never')
	#tk.messagebox.askokcancel(title='Hi', message='never')
# tk.Button(window,text='hit me',command=hit_me).pack()


# window.mainloop()
#---------------------------------------------
#放置地点
# import tkinter.messagebox 
# import tkinter as tk
# window=tk.Tk()
# window.title('my window')
# window.geometry('200x200')
# tk.Label(window,text=1).place(x=10,y=100,anchor='center')
# tk.Label(window,text=1).pack(side='bottom')
# tk.Label(window,text=1).pack(side='left')
# tk.Label(window,text=1).pack(side='right')
# for i in range(4):
	# for j in range(3):
		# tk.Label(window,text=1).grid(row=i,column=j,ipadx=10,ipady=10)
# window.mainloop()
#----------------------------------------------
#实践环节
# import tkinter.messagebox 
# import tkinter as tk
# import pickle
# window=tk.Tk()
# window.title('Welcome to this place')
# window.geometry('450x300')
# canvas=tk.Canvas(window,height=200,width=500)
# image_file=tk.PhotoImage(file=r'C:\Users\shouw\Pictures\jojo.gif')
# image=canvas.create_image(0,0,anchor='nw',image=image_file)
# canvas.pack(side='top')
# tk.Label(window,text='User name:').place(x=50,y=150)
# tk.Label(window,text='Password:').place(x=50,y=190)
# var_usr_name=tk.StringVar()
# var_usr_name.set('example@python.com')
# var_usr_pwd=tk.StringVar()
# entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
# entry_usr_name.place(x=160,y=150)
# entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
# entry_usr_pwd.place(x=160,y=190)
# login and sign up button
# def usr_login():
    # usr_name = var_usr_name.get()
    # usr_pwd = var_usr_pwd.get()
    # try:
        # with open('D:/usrs_info.txt', 'rb') as usr_file:
            # usrs_info = pickle.load(usr_file)
    # except FileNotFoundError:
        # with open('D:/usrs_info.txt', 'wb') as usr_file:
            # usrs_info = {'admin': 'admin'}
            # pickle.dump(usrs_info, usr_file)
    # if usr_name in usrs_info:
        # if usr_pwd == usrs_info[usr_name]:
            # tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        # else:
            # tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    # else:
        # is_sign_up = tk.messagebox.askyesno('Welcome',
                               # 'You have not signed up yet. Sign up today?')
        # if is_sign_up:
            # usr_sign_up()

# def usr_sign_up():
    # def sign_to_Mofan_Python():
        # np = new_pwd.get()
        # npf = new_pwd_confirm.get()
        # nn = new_name.get()
        # with open('D:/usrs_info.txt', 'rb') as usr_file:
            # exist_usr_info = pickle.load(usr_file)
            # pickle.dump(exist_usr_info, usr_file)
        # if np != npf:
            # tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        # elif nn in exist_usr_info:
            # tk.messagebox.showerror('Error', 'The user has already signed up!')
        # else:
            # exist_usr_info[nn] = np
            # with open('D:/usrs_info.txt', 'wb') as usr_file:
                # pickle.dump(exist_usr_info, usr_file)
            # tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # window_sign_up.destroy()
    # window_sign_up = tk.Toplevel(window)
    # window_sign_up.geometry('350x200')
    # window_sign_up.title('Sign up window')

    # new_name = tk.StringVar()
    # new_name.set('example@python.com')
    # tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    # entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    # entry_new_name.place(x=150, y=10)

    # new_pwd = tk.StringVar()
    # tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    # entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    # entry_usr_pwd.place(x=150, y=50)

    # new_pwd_confirm = tk.StringVar()
    # tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    # entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    # entry_usr_pwd_confirm.place(x=150, y=90)

    # btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    # btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
# btn_login = tk.Button(window, text='Login', command=usr_login)
# btn_login.place(x=170, y=230)
# btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
# btn_sign_up.place(x=270, y=230)

# window.mainloop()


import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='C:/Users/shouw/Pictures/jojo.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('D:/data-part2/usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('D:/data-part2/usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                               'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to_zxy_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('D:/data-part2/usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('D:/data-part2/usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_zxy_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()