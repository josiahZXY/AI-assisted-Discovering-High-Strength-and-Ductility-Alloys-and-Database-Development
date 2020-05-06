# 应力应变曲线
# import pandas as pd
# df['x3']=df[['E','Y']].apply(lambda x:((x['Y']/x['E'])+0.2),axis=1)
# df['x0']=df[['x3']].apply(lambda x:((x['x3']+0.2)),axis=1)
# df['x2']=df[['E','Y','El']].apply(lambda x:((x['Y']/x['E'])+x['El']),axis=1)
# df['x1']=df[['x0','x2']].apply(lambda x:((x['x0']+x['x2'])/2),axis=1)

# df['a']=df[['x0','x1','x2','Y','U']].apply(lambda x:(((x['Y']-x['U'])*(x['x2']-x['x0']))/(((x['x2']*x['x2'])-(x['x0'])*x['x2']-(x['x1']*x['x2'])+(x['x1']*x['x0']))*(x['x1']-x['x0']))),axis=1)
# df['b']=df[['x0','x1','a','Y','U']].apply(lambda x:((x['U']-x['Y']+(x['a']*x['x0']*x['x0'])-(x['a']*x['x1']*x['x1']))/(x['x1']-x['x0'])),axis=1)
# df['c']=df[['b','x0','a','Y']].apply(lambda x:((x['Y']-(x['b']*x['x0'])-x['a']*x['x0']*x['x0'])),axis=1)
# x['Y']
# x['U']
# x['x0']
# x['x1']
# x['x2']
# x['a']
# x['b']
# ((x['Y']-x['U'])*(x['x2']-x['x0']))/(((x['x2']*x['x2'])-(x['x0'])*x['x2']-(x['x1']*x['x2'])+(x['x1']*x['x0']))*(x['x1']-x['x0']))

# (x['U']-x['Y']+(x['a']*x['x0']*x['x0'])-(x['a']*x['x1']*x['x1']))/(x['x1']-x['x0'])

# (x['Y']-(x['b']*x['x0'])-x['a']*x['x0']*x['x0'])

# import matplotlib.pyplot as plt 
# import numpy as np
# x=np.arange(1.88,19.13,0.01)
# y=(-8.49)*x**2+178.49*x+199.3
# x1=np.arange(0,1.88,0.01)
# y1=268.16*x1
# plt.figure()
# plt.plot(x1,y1)
# plt.plot(x,y)
# plt.xlabel("elongation")
# plt.ylabel("Tensile Strength")
# plt.title("mp-672259")
# plt.show()

# df.iat[i,5],df.iat[i,6]
# df.iat[i,8] df.iat[i,9]  df.iat[i,10]
# 0 df.iat[i,5]
# df.iat[i,1]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df=pd.read_csv('D:/data-part2/quxianbasicdata.csv')
for i in range(0,5):
	x=np.arange(df.iat[i,5],df.iat[i,6],0.01)
	y=(df.iat[i,8])*x**2+(df.iat[i,9])*x+df.iat[i,10]
	x1=np.arange(0,df.iat[i,11],0.01)
	y1=(df.iat[i,1])*x1
	y2=np.arange(df.iat[i,3],(df.iat[i,1]*df.iat[i,11]),0.01)
	x2=df.iat[i,11]+y2*0
	x3=[[df.iat[i,11],df.iat[i,5]]]
	y3=[[df.iat[i,3],df.iat[i,3]]]
	plt.figure()
	plt.plot(x1,y1)
	plt.plot(x,y)
	plt.plot(x2,y2)
	for n in range(len(x3)):
		plt.plot(x3[n], y3[n], color='r')
		#plt.scatter(x3[n], y3[n], color='b')
	plt.xlabel("elongation")
	plt.ylabel("Tensile Strength")
	plt.title("%s"%df.iat[i,0])
	plt.plot(df.iat[i,5], df.iat[i,3], '.y')
	plt.annotate('Tensile Strength,Yield', xy=(df.iat[i,5], df.iat[i,3]), xytext=(df.iat[i,5]+2, df.iat[i,3] + 50), arrowprops=dict(arrowstyle='->'))
	plt.annotate('(%s , %s)'%(df.iat[i,5],df.iat[i,3]), xy=(df.iat[i,5], df.iat[i,3]), xytext=(df.iat[i,5]-1, df.iat[i,3]+30))
	plt.plot(df.iat[i,7], df.iat[i,2], '.y')
	plt.annotate('Tensile Strength,Ultimate', xy=(df.iat[i,7], df.iat[i,2]), xytext=(df.iat[i,7]+2, df.iat[i,2]), arrowprops=dict(arrowstyle='->'))
	plt.annotate('(%s , %s)'%(df.iat[i,7],df.iat[i,2]), xy=(df.iat[i,7], df.iat[i,2]), xytext=(df.iat[i,7]-1, df.iat[i,2]-50))
	plt.plot(df.iat[i,4],0, '.y')
	plt.annotate('Elongation at break', xy=(df.iat[i,4], 0), xytext=(df.iat[i,6]-1, 50), arrowprops=dict(arrowstyle='->'))
	plt.annotate('(%s , 0)'%df.iat[i,4], xy=(df.iat[i,4], 0), xytext=(df.iat[i,4]-1, 20))
	plt.savefig('D:/data-part2/quxian/%s.png'%df.iat[i,0],bbox_inches='tight')