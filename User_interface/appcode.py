from __future__ import print_function
import warnings
warnings.filterwarnings('ignore')
import ctypes, sys
#ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
import pickle
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
import os
from sklearn.model_selection import train_test_split
#from automatminer import MatPipe
import time
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename
from PIL import Image
import matplotlib.pyplot as plt
import webbrowser
from shutil import copyfile
import tkinter
#webbrowser.open(r'C:\Users\zhang\Desktop\machine_learning_way.docx')
window = tk.Tk()
window.title('Welcome to crystal Pre')
window.geometry('710x500')
tabControl=ttk.Notebook(window)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Introduction')
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='Machine Learning predict')
tab3=ttk.Frame(tabControl)
tabControl.add(tab3,text='Deep learning predict')
tab4=ttk.Frame(tabControl)
tabControl.add(tab4,text='search from database')
tab5=ttk.Frame(tabControl)
tabControl.add(tab5,text='plot the stress_strain curves')
tabControl.pack(expand=1,fill="both")
pchoose='D:/FYP_files/Deep_learning/cgcnn-master/pre-trained/Ultimate.pth.tar'

# def selectPath():
    # path_ = askdirectory()
    # path.set(path_)
# path = StringVar()
# Label(window,text = "目标路径:").grid(row = 10, column = 0)
# Entry(window, textvariable = path).grid(row = 10, column = 1)
# Button(window, text = "路径选择", command = selectPath).grid(row = 10, column = 2)
a=''
naming='Ultimate'
def selectPath():
	path_=askdirectory()
	path.set(path_)
	global a
	a=path_
path=StringVar()
def dl_prediction1():
	a1='cd D:/FYP_files/Deep_learning/cgcnn-master && python D:/FYP_files/Deep_learning/cgcnn-master/predict.py %s %s'%(pchoose,a)
	#格式为a='cd C:/Users/zhang/cgcnn-master && python predict.py pre-trained/Ultimate.pth.tar C:/Users/zhang/mt-cgcnn-master/data/ts_Ultimate'
	d=os.system(a1)
	df=pd.read_csv(r'D:\FYP_files\Deep_learning\test_results.csv')
	if naming=='Ultimate':
		df.columns=['id','number','Tensile Strength, Ultimate predicted']
		del df['number']
		df=df.dropna(axis=0,how='all')
		df.to_csv('%s/Ultimate.csv'%d3)
	elif naming=='Yield':
		df.columns=['id','number','Tensile Strength, Yield predicted']
		del df['number']
		df=df.dropna(axis=0,how='all')
		df.to_csv('%s/Yield.csv'%d3)
	elif naming=='Elongation':
		df.columns=['id','number','Elongation at Break predicted']
		del df['number']
		df=df.dropna(axis=0,how='all')
		df.to_csv('%s/Elongation.csv'%d3)
	elif naming=='K_VRH':
		df.columns=['id','number','elasticity.K_VRH predicted']
		del df['number']
		df=df.dropna(axis=0,how='all')
		df.to_csv('%s/K_VRH.csv'%d3)
	elif naming=='G_VRH':
		df.columns=['id','number','elasticity.G_VRH predicted']
		del df['number']
		df=df.dropna(axis=0,how='all')
		df.to_csv('%s/G_VRH.csv'%d3,index=False)
	os.startfile('%s'%d3)
#--------------------------------------------
path2=StringVar()
d3=''
def dlselectpath():
	path_=askdirectory()
	path2.set(path_)
	global d3
	d3=path_
#--------------------------------------------
intro=ttk.LabelFrame(tab1,text='About this software')
intro.grid(column=0,row=0,padx=8,pady=4)
i_label=ttk.Label(intro,text="Welcome to the prediction software for stress-strain curve of alloy and crystal")
i_label.grid(column=0,row=0,sticky='W')
# i1_label=ttk.Label(intro,text='在机器学习预测面板，输入晶体的composition即可获得单个晶体的应力应变曲线数据预测结果,如果您需要做大量预测，也可以按照左上角help中的介绍做一个专\n门的csv文件进行大量预测,预测结果会返回一个csv文件以及一个文件夹，其中csv\n文件包含有弹性性质量6个，塑形性质量3个，文件夹中包含所有预测结果的应力\n应变曲线图可供参考')
i1_label=ttk.Label(intro,text='In the machine learning prediction panel, you can input the crystal composition to obtain the stress-strain curve data\n prediction results of a single crystal,If you need to make a lot of predictions, you can also make a special CSV file\n to make a lot of predictions as described in "Help" in the upper left corner. The prediction results will return a CSV\n file and a folder，There are 6 elastic masses and 3 plastic masses in the CSV file. The folder contains the stress-strain\n curves of all predicted results for reference')
i1_label.grid(column=0,row=1,sticky='W')
# i2_label=ttk.Label(intro,text='在深度学习预测面板，请先按照help中的叮嘱，做成如图所示的一个文件夹，再在\n面板内选择该文件夹，并选择一个自己想要预测的性质，预测结果会显示在您所在\n的文件夹内，如果想要绘图，请在预测完所有性质后，将csv预测文件放入同一个\n文件夹下，并选择plot，即可绘图')
i2_label=ttk.Label(intro,text='In the deep learning prediction panel, please make a folder as shown in the figure according to the instructions in\n "Help" first, then select the folder in the panel, and select a property you want to predict, the prediction results will be\n displayed in your folder. If you want to draw, please put the CSV prediction file into the same folder after predicting\n all properties, and prepare for the next step')
i2_label.grid(column=0,row=2,sticky='W')
# i3_label=ttk.Label(intro,text='在搜索面板中，您可以通过mp-id来搜索http://www.materialsproject.org内所存\n在的晶体的弹性和塑形数据，并且查看经过程序运算后所打出来的图，程序内有大\n概8000个晶体的图片，后续会继续更新')
i3_label=ttk.Label(intro,text='In the search panel, you can search the elastic and plastic data of crystals calculated by myself and as the basic\n materials are all from http://www.materialsproject.org through mp-id, so you can input the material_id to search the\n treated crystals. There are pictures of about 8000 crystals in the program, which will be updated later')
i3_label.grid(column=0,row=3,sticky='W')
i4_label=ttk.Label(intro,text='Hope you have a good time, thank you!')
i4_label.grid(column=0,row=4,sticky='W')
i5_label=ttk.Label(intro,text='Author:Zhang Xiaoyang academic advisor:Shen lei')
i5_label.grid(column=0,row=5,sticky='W')
dl=ttk.LabelFrame(tab3,text='Deep learning pre')
dl.grid(column=0,row=0,padx=8,pady=4)
a_label=ttk.Label(dl,text="Source path")
a_label.grid(column=0,row=0,sticky='W')
path_entered=ttk.Entry(dl,width=20,textvariable=path)
path_entered.grid(column=0,row=1,sticky='W')
action1=ttk.Button(dl,text='choose the path',command=selectPath)
action1.grid(column=2,row=1)
action2=ttk.Button(tab3,text='Predict',command=dl_prediction1)
action2.place(x=270,y=180,width=100,height=100)
#--------------------------------
dlplot=ttk.LabelFrame(tab3,text='Please select results storage folder')
dlplot.place(x=0,y=180)
dlplot_label=ttk.Label(dlplot,text='choose path for results')
dlplot_label.grid(column=0,row=2,sticky='W')
dlplot_entered=ttk.Entry(dlplot,width=20,textvariable=path2)
dlplot_entered.grid(column=0,row=3,sticky='W')
dlplot_action=ttk.Button(dlplot,text='choose the path',command=dlselectpath)
dlplot_action.grid(column=2,row=3)
#--------------------------------
def radCall():
	radSel=radVar.get()
	global pchoose
	global naming
	if radSel == 0:
		pchoose='D:/FYP_files/Deep_learning/cgcnn-master/pre-trained/Ultimate.pth.tar'
		naming='Ultimate'
	elif radSel == 1:
		pchoose='D:/FYP_files/Deep_learning/cgcnn-master/pre-trained/yield_best.pth.tar'
		naming='Yield'
	elif radSel == 2:
		pchoose='D:/FYP_files/Deep_learning/cgcnn-master/pre-trained/elongation_best.pth.tar'
		naming='Elongation'
	elif radSel == 3:
		pchoose='D:/FYP_files/Deep_learning/cgcnn-master/pre-trained/K_best.pth.tar'
		naming='K_VRH'
	elif radSel == 4:
		pchoose='D:/FYP_files/Deep_learning/cgcnn-master/pre-trained/G_best.pth.tar'
		naming='G_VRH'
radVar=tk.IntVar()
colors=["ts_Ultimate","ts_Yield","Elongation at break","K_VRH","G_VRH"]
for col in range(5):
	curRad=tk.Radiobutton(dl,text=colors[col],variable=radVar,value=col,command=radCall)
	curRad.grid(column=4,row=col,sticky=tk.W)
# lb1=tk.Label(window,text = "目标路径:").place(x=50, y= 150)
# en1=tk.Entry(window, textvariable = path).place(x=120, y= 150)
# bnt1=tk.Button(window, text = "路径选择", command = selectPath).place(x=250, y= 150)
chosen='ts_Ultimate'
def mlchoose(event):
    global chosen
    chosen=prestr_list.get()
def click_me():
	idata=composition.get()
	if chosen == 'ts_Ultimate':
		a2='python D:/FYP_files/User_interface/ml_pre.py %s %s'%(idata,m3)
		d1=os.system(a2)
		print(d1)
	elif chosen == 'ts_Yield':
		a2='python D:/FYP_files/User_interface/ml2_pre.py %s %s'%(idata,m3)
		d1=os.system(a2)
		print(d1)
	elif chosen == 'Elongation':
		a2='python D:/FYP_files/User_interface/ml3_pre.py %s %s'%(idata,m3)
		d1=os.system(a2)
	elif chosen =='K_VRH':
		a2='python D:/FYP_files/User_interface/ml4_pre.py %s %s'%(idata,m3)
		d1=os.system(a2)
	else:
		a2='python D:/FYP_files/User_interface/ml5_pre.py %s %s'%(idata,m3)
		d1=os.system(a2) 
	os.startfile('%s'%m3)
    # df=pd.DataFrame(idata)
    # filename ='C:/Users/zhang/MatPipe_predict_third_time_Ultimate_from_composition.p'
    # pipe = MatPipe.load(filename)
    # time.sleep(20)
    # df = pipe.predict(df)
    # df.to_csv('C:/Users/zhang/results.csv')
ml=ttk.LabelFrame(tab2,text="Machine learning pre")
ml.grid(column=0,row=0,padx=8,pady=4)
ml_label=ttk.Label(ml,text="composition")
ml_label.grid(column=0,row=0,sticky='W')
composition=tk.StringVar()
comp_entered=ttk.Entry(ml,width=20,textvariable=composition)
comp_entered.grid(column=0,row=1,sticky='W')
comp_action=ttk.Button(tab2,text="prediction",command=click_me)
#comp_action.grid(column=0,row=2,sticky='W')
comp_action.place(x=500,y=0,width=75,height=75)
    #filename=''
ml_opt=ttk.LabelFrame(tab2,text="predicted options")
ml_opt.grid(column=1,row=0,padx=8,pady=4)
ttk.Label(ml_opt,text='pre result:').grid(column=0,row=0)
prestr=tk.StringVar()
prestr_list=ttk.Combobox(ml_opt,width=18,textvariable=ml_opt,state='readonly')
prestr_list['values']=('ts_Ultimate','ts_Yield','Elongation','K_VRH','G_VRH')
mp_id=tk.StringVar()
prestr_list.current(0)
prestr_list.bind("<<ComboboxSelected>>",mlchoose)
prestr_list.grid(column=1,row=1)
ml2=ttk.LabelFrame(tab2,text='csv Machine learning pre')
ml2.place(x=0,y=120)
path1=StringVar()
m=''
chosen2='ts_Ultimate'
def selectPath1():
	path_=askopenfilename()
	path1.set(path_)
	global m
	m=path_
def mlchoose2(event):
	global chosen2
	chosen2=prestr2_list.get()
def ml_prediction():
	if chosen2 == 'ts_Ultimate':
		ppt='MatPipe_predict_Ultimate_fourthtime_from_composition.p'
		a3='python D:/FYP_files/User_interface/manyfile.py %s %s %s'%(m,ppt,m3)
		d2=os.system(a3)
		print(d2)
	elif chosen2 == 'ts_Yield':
		ppt='MatPipe_predict_Fourthpre_Yield_from_composition.p'
		a3='python D:/FYP_files/User_interface/manyfile.py %s %s %s'%(m,ppt,m3)
		d2=os.system(a3)
		print(d2)
	elif chosen2 == 'Elongation':
		ppt='MatPipe_predict_thirdelongation_from_composition.p'
		a3='python D:/FYP_files/User_interface/manyfile.py %s %s %s'%(m,ppt,m3)
		d2=os.system(a3)
		print(d2)
	elif chosen2 == 'K_VRH':
		ppt='MatPipe_predict_elasticity.K_VRH_from_composition.p'
		a3='python D:/FYP_files/User_interface/manyfile.py %s %s %s'%(m,ppt,m3)
		d2=os.system(a3)
		print(d2)
	else:
		ppt='MatPipe_predict_finalelasticity.G_VRH_from_composition.p'
		a3='python D:/FYP_files/User_interface/manyfile.py %s %s %s'%(m,ppt,m3)
		d2=os.system(a3)
		print(d2)
	os.startfile('%s'%m3)
ml2_label=ttk.Label(ml2,text="Source path")
ml2_label.grid(column=0,row=0,sticky='W')
ml2_path_entered=ttk.Entry(ml2,width=20,textvariable=path1)
ml2_path_entered.grid(column=0,row=1,sticky='W')
ml2_action1=ttk.Button(ml2,text='Choose the path',command=selectPath1)
ml2_action1.grid(column=0,row=2)
ml2_action2=ttk.Button(tab2,text='prediction',command=ml_prediction)
ml2_action2.place(x=500,y=120,width=75,height=75)
ml2_opt=ttk.LabelFrame(tab2,text="Option")
ml2_opt.place(x=175,y=120)
ttk.Label(ml2_opt,text='predicted result: ').grid(column=0,row=0)
prestr2=tk.StringVar()
prestr2_list=ttk.Combobox(ml2_opt,width=18,textvariable=ml2_opt,state='readonly')
prestr2_list['values']=('ts_Ultimate','ts_Yield','Elongation','K_VRH','G_VRH')
prestr2_list.current(0)
prestr2_list.bind("<<ComboboxSelected>>",mlchoose2)
prestr2_list.grid(column=1,row=1)
line_label=ttk.Label(tab2,text='----------------------------------------------------------------------------------------------')
line_label.place(x=0,y=220)
#--------------------------------------------
path3=StringVar()
m3=''
def mlselectpath():
	path_=askdirectory()
	path3.set(path_)
	global m3
	m3=path_

mlplot=ttk.LabelFrame(tab2,text='Select result storage folder')
mlplot.place(x=0,y=240)
mlplot_label=ttk.Label(mlplot,text='choose path for results')
mlplot_label.grid(column=0,row=0,sticky='W')
mlplot_entered=ttk.Entry(mlplot,width=20,textvariable=path3)
mlplot_entered.grid(column=0,row=1,sticky='W')
mlplot_action=ttk.Button(mlplot,text='choose the path',command=mlselectpath)
mlplot_action.grid(column=2,row=1)

#---------------------------------------------
path4=StringVar()
def pre_click():
    huoqu=mp_id.get()
    i={'material_id':[huoqu]}
    df3=pd.DataFrame(i)
    df4=pd.read_csv('D:/FYP_files/database/data_after_processing/quxian_database.csv')
    df5=pd.merge(df3,df4)
    if df5.empty==True:
        Receive_Window.insert("end",'no match'+'\n')
        Receive_Window.see("end")
    else:
        Receive_Window.insert("end",str(df5.iloc[0])+'\n')
        Receive_Window.see("end")
        # img=Image.open(r'D:\FYP_files\database\data_after_processing\quxian\%s.png'%huoqu)
        # plt.figure("%s"%huoqu)
        # plt.imshow(img)
        # plt.show()
    if df5.empty==True:
        pass
    else:
        img=Image.open(r'D:\FYP_files\database\data_after_processing\quxian\%s.png'%huoqu)
        plt.figure("%s"%huoqu)
        plt.imshow(img)
        plt.show()
def soutput():
    huoqu=mp_id.get()
    i={'material_id':[huoqu]}
    df3=pd.DataFrame(i)
    df4=pd.read_csv(r'D:\FYP_files\database\data_after_processing\quxian_database.csv')
    df5=pd.merge(df3,df4)
    if df5.empty==True:
        result =tkinter.messagebox.showerror(title = 'Wrong！',message='The material is not in the database')
    else:
        path_=askdirectory()
        path4.set(path_)
        copyfile(r'D:\FYP_files\database\data_after_processing\quxian\%s.png'%huoqu, '%s/%s.png'%(path_,huoqu))
        df5.to_csv('%s/%s.csv'%(path_,huoqu))
search=ttk.LabelFrame(tab4,text="Material Search")
search.grid(column=0,row=0,padx=8,pady=4)
search_label=ttk.Label(search,text='input mp-id')
search_label.grid(column=0,row=0,sticky='W')
search_entered=ttk.Entry(search,width=20,textvariable=mp_id)
search_entered.grid(column=0,row=1,sticky='W')
search_button=ttk.Button(search,text='start search',command=pre_click)
search_button.grid(column=1,row=1,sticky='W')
Receive=tk.LabelFrame(tab4,text="output",padx=10,pady=10)
Receive.place(x=125,y=100)
Receive_Window=scrolledtext.ScrolledText(Receive,width=40,height=15,padx=8,pady=10,wrap=tk.WORD)
Receive_Window.grid()
search_button2=ttk.Button(tab4,text='save as...',command=soutput)
search_button2.place(x=50,y=400)
#copyfile(r'D:\AI_Fina_Year_Project\Gui\Elongation.csv', r'D:\AI_Fina_Year_Project\Elongation.csv')
#
#-------------------------------------------------------------------
tpath=StringVar()
tpath2=StringVar()
tpath3=StringVar()
tpath4=StringVar()
tpath5=StringVar()
tpath6=StringVar()
t=''
t2=''
t3=''
t4=''
t5=''
t6=''
def tselectpath():
	tpath_=askopenfilename()
	tpath.set(tpath_)
	global t
	t=tpath_
tplot=ttk.LabelFrame(tab5,text='Stress-strain curves')
tplot.grid(column=0,row=0,padx=8,pady=4)
tplot_label1=ttk.Label(tplot,text='choose path of Ultimate')
tplot_label1.grid(column=0,row=0,sticky='W')
tplot_entered1=ttk.Entry(tplot,width=20,textvariable=tpath)
tplot_entered1.grid(column=0,row=1,sticky='W')
tplot_action1=ttk.Button(tplot,text='choose the path',command=tselectpath)
tplot_action1.grid(column=2,row=1)
#-------------------------------------------------
def tselectpath2():
	tpath_=askopenfilename()
	tpath2.set(tpath_)
	global t2
	t2=tpath_
tplot_label2=ttk.Label(tplot,text='choose path of Yield')
tplot_label2.grid(column=0,row=2,sticky='W')
tplot_entered2=ttk.Entry(tplot,width=20,textvariable=tpath2)
tplot_entered2.grid(column=0,row=3,sticky='W')
tplot_action2=ttk.Button(tplot,text='choose the path',command=tselectpath2)
tplot_action2.grid(column=2,row=3)
#----------------------------------------------------
def tselectpath3():
	tpath_=askopenfilename()
	tpath3.set(tpath_)
	global t3
	t3=tpath_
tplot_label3=ttk.Label(tplot,text='choose path of Elongation')
tplot_label3.grid(column=0,row=4,sticky='W')
tplot_entered3=ttk.Entry(tplot,width=20,textvariable=tpath3)
tplot_entered3.grid(column=0,row=5,sticky='W')
tplot_action3=ttk.Button(tplot,text='choose the path',command=tselectpath3)
tplot_action3.grid(column=2,row=5)
#----------------------------------------------
def tselectpath4():
	tpath_=askopenfilename()
	tpath4.set(tpath_)
	global t4
	t4=tpath_
tplot_label4=ttk.Label(tplot,text='choose path of K_VRH')
tplot_label4.grid(column=0,row=6,sticky='W')
tplot_entered4=ttk.Entry(tplot,width=20,textvariable=tpath4)
tplot_entered4.grid(column=0,row=7,sticky='W')
tplot_action4=ttk.Button(tplot,text='choose the path',command=tselectpath4)
tplot_action4.grid(column=2,row=7)
#-----------------------------------------
def tselectpath5():
	tpath_=askopenfilename()
	tpath5.set(tpath_)
	global t5
	t5=tpath_
tplot_label5=ttk.Label(tplot,text='choose path of G_VRH')
tplot_label5.grid(column=0,row=8,sticky='W')
tplot_entered5=ttk.Entry(tplot,width=20,textvariable=tpath5)
tplot_entered5.grid(column=0,row=9,sticky='W')
tplot_action5=ttk.Button(tplot,text='choose the path',command=tselectpath5)
tplot_action5.grid(column=2,row=9)
#--------------------------------------------
def tselectpath6():
	tpath_=askdirectory()
	tpath6.set(tpath_)
	global t6
	t6=tpath_
tplot2=ttk.LabelFrame(tab5,text='Select results storage folder')
tplot2.grid(column=1,row=0,padx=8,pady=4)
tplot_label6=ttk.Label(tplot2,text='choose path for results')
tplot_label6.grid(column=0,row=0,sticky='W')
tplot_entered6=ttk.Entry(tplot2,width=20,textvariable=tpath6)
tplot_entered6.grid(column=0,row=1,sticky='W')
tplot_action6=ttk.Button(tplot2,text='choose the path',command=tselectpath6)
tplot_action6.grid(column=2,row=1)
#--------------------------------------------
def startplot():
	a='python D:/FYP_files/User_interface/plottime.py %s %s %s %s %s %s'%(t,t2,t3,t4,t5,t6)
	d=os.system(a)
tplot_button=ttk.Button(tab5,text="Start painting",command=startplot)
tplot_button.place(x=100,y=300,width=300,height=100)
#ml_enter=ttk.Entry()
#---------------------------------------------
def guideml():
	webbrowser.open(r'D:\FYP_files\User_interface\guidebook\machine_learning_way.docx')
	# top=Toplevel()
	# top.title('Machine_Learning guidance')
	# top.geometry('550x500')
	# msg=Message(top,text='ml')
	# msg.pack()
#--------------------------------------------
def guidedl():
	webbrowser.open(r'D:\FYP_files\User_interface\guidebook\Deep_learning_way.docx')
	# top=Toplevel()
	# top.title('Deep_Learning guidance')
	# top.geometry('550x500')
	# msg=Message(top,text='dl')
	#msg.pack()
#--------------------------------------------
def guidesc():
	webbrowser.open(r'D:\FYP_files\User_interface\guidebook\search_way.docx')
	# top=Toplevel()
	# top.title('Search guidance')
	# top.geometry('550x500')
	# gsc=ttk.LabelFrame(top,text="search页面使用简介")
	# gsc.grid(column=0,row=0,padx=8,pady=4)
	# msg=ttk.Label(gsc,text='1.在搜索面板，请您将material id输入到搜索框内')
	# msg.grid(column=0,row=0,sticky='W')
	# msg2=ttk.Label(gsc,text="	格式: mp-9578")
	# msg3=ttk.Label(gsc,text='2.点击search')
	# msg4=ttk.Label(gsc,text='	若没有搜索结果,则会在框中打出 no match')
	# msg5=ttk.Label(gsc,text='	若有搜索结果,则会在框中打出材料的弹性和塑性性质，以及材料的预测应力应变曲线')
	# msg2.grid(column=0,row=1,sticky='W')
	# msg3.grid(column=0,row=2,sticky='W')
	# msg4.grid(column=0,row=3,sticky='W')
	# msg5.grid(column=0,row=4,sticky='W')
#--------------------------------------------
def guideplo():
	webbrowser.open(r'D:\FYP_files\User_interface\guidebook\ploting_way.docx')
	# top=Toplevel()
	# top.title('Plotting guidance')
	# top.geometry('550x500')
	# msg=Message(top,text='plo')
	# msg.pack()
#--------------------------------------------
menubar = Menu(window)
window.config(menu=menubar)
help_menu = Menu(menubar,tearoff=False)
help_menu.add_command(label="Machine_Learning",command=guideml)
help_menu.add_command(label="Deep_Learning",command=guidedl)
help_menu.add_command(label="Search",command=guidesc)
help_menu.add_command(label="Plotting",command=guideplo)
menubar.add_cascade(label='Help',menu=help_menu)

window.mainloop()