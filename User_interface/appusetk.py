import tkinter as tk
window=tk.Tk()
window.title('my window')
window.geometry('200x200')
canvas=tk.Canvas(window,bg="blue",height=500,width=500)
image_file=tk.PhotoImage(file=r'C:\Users\shouw\Pictures\jojo.gif')
image=canvas.create_image(0,0,anchor="nw",image=image_file)
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1)
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=180)
rect=canvas.create_rectangle(100,30,100+20,30+20)
canvas.pack()
def moveit():
	canvas.move(rect,0,2)
b=tk.Button(window,text='move',command=moveit).pack()

# var=tk.StringVar()
# l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
# l.pack()
# on_hit=False
# def hit_me():
	# global on_hit
	# if on_hit==False:
		# on_hit=True
		# var.set('you hit me')
	# else:
		# on_hit=False
		# var.set("")
# b=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
# b.pack()
# window.mainloop()#点击一次，更新一下
# e=tk.Entry(window,show=None)#show='*'指的是输入类似于密码形式
# e.pack()
# var=tk.StringVar()

# var1=tk.StringVar()
# l=tk.Label(window,bg='yellow',width=20,text="empty")
# l.pack()
# def print_seleciton():
	# l.config(text='you have selected'+var.get())
	# l.config(text='you have selected' + v)
	# if(var1.get()==1)and(var2.get()==0):
		# l.config(text='I love only python')
	# elif(var1.get()==0)and(var2.get()==1):
		# l.config(text='I love only C++')
	# elif (var1.get()==0)and(var2.get()==0):
		# l.config(text='I do not love either')
	# else:
		# l.config(text='I love both')
# r1=tk.Radiobutton(window,text='Option A',variable=var,value='A',comman=print_seleciton)
# r1.pack()
# r2=tk.Radiobutton(window,text='Option B',variable=var,value='B',comman=print_seleciton)
# r2.pack()
# r3=tk.Radiobutton(window,text='Option C',variable=var,value='C',comman=print_seleciton)
# r3.pack()
# s=tk.Scale(window,label='try me', from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=2,resolution=0.01,command=print_seleciton)
# s.pack()
# var1=tk.IntVar()
# var2=tk.IntVar()
# c1=tk.Checkbutton(window,text='python',variable=var1,onvalue=1,offvalue=0,command=print_seleciton)
# c2=tk.Checkbutton(window,text='c++',variable=var2,onvalue=1,offvalue=0,command=print_seleciton)
# c1.pack()
# c2.pack()

# def print_selection():
	# value=lb.get(lb.curselection())
	# var1.set(value)
# def insert_point():
	# var=e.get()
	# t.insert('insert',var)
# def insert_end():
	# var=e.get()
	# t.insert('end',var)
# b1=tk.Button(window,text="print selection",width=15,height=6,command=print_selection)
# b1.pack()
# var2=tk.StringVar()
# var2.set((11,22,33,44))
# lb=tk.Listbox(window,listvariable=var2)
# list_items=[1,2,3,4]
# for item in list_items:
	# lb.insert('end',item)
# lb.insert(1,'first')
# lb.insert(2,'second')
# lb.delete(2)
# lb.pack()
# b2=tk.Button(window,text="insert end",width=15,height=2,command=insert_end)
# b2.pack()
# t=tk.Text(window,height=2)
# t.pack()
window.mainloop()