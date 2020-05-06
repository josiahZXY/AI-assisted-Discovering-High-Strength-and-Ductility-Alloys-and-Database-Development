import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('D:/FYP_files/Deep_learning/cgcnn-master/cnn_K_VRH.csv')
df=df.dropna(axis=0,how='all')
df.index=[i for i in range(df.shape[0])]
df=df.sort_values(by='NK_VRH',ascending=True)
x1=df['NK_VRH']
y1=df['NK_VRH']
y2=df['K_VRH']
df2=pd.read_csv('D:/FYP_files/Deep_learning/cgcnn-master/cnn_G_VRH.csv')
df2=df2.dropna(axis=0,how='all')
df2.index=[i for i in range(df2.shape[0])]
df2=df2.sort_values(by='NG_VRH',ascending=True)
x2=df2['NG_VRH']
y3=df2['NG_VRH']
y4=df2['G_VRH']
plt.figure()
plt.plot(x1,y1)
plt.scatter(x1,y2)
plt.xlabel("normal K_VRH")
plt.ylabel("predicted K_VRH")
plt.title("comparisionK")
plt.figure()
plt.plot(x2,y3)
plt.scatter(x2,y4)
plt.xlabel("normal G_VRH")
plt.ylabel("predicted G_VRH")
plt.title("comparisionG")
plt.show()
#df1.rename(columns={'c':'D'},inplace=True)
