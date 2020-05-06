import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
p1=sys.argv[1]
p2=sys.argv[2]
p3=sys.argv[3]
p4=sys.argv[4]
p5=sys.argv[5]
p6=sys.argv[6]
df1=pd.read_csv(p1)
df2=pd.read_csv(p2)
df3=pd.read_csv(p3)
df4=pd.read_csv(p4)
df5=pd.read_csv(p5)
df1=pd.DataFrame(df1,columns=['id','Tensile Strength, Ultimate predicted'])
df2=pd.DataFrame(df2,columns=['id','Tensile Strength, Yield predicted'])
df3=pd.DataFrame(df3,columns=['id','Elongation at Break predicted'])
df4=pd.DataFrame(df4,columns=['id','elasticity.K_VRH predicted'])
df5=pd.DataFrame(df5,columns=['id','elasticity.G_VRH predicted'])
df=pd.merge(df1,df2)
df=pd.merge(df,df3)
df=pd.merge(df,df4)
df=pd.merge(df,df5)
df['youngs']=df[["elasticity.K_VRH predicted","elasticity.G_VRH predicted"]].apply(lambda x:(9*x["elasticity.K_VRH predicted"]*x["elasticity.G_VRH predicted"])/(3*x["elasticity.K_VRH predicted"]+x["elasticity.G_VRH predicted"]),axis=1)
df['poisson rate']=df[["elasticity.K_VRH predicted","youngs"]].apply(lambda x:(3*x["elasticity.K_VRH predicted"]-x["youngs"])/(6*x["elasticity.K_VRH predicted"]),axis=1)
df['flexibility']=df[["poisson rate","youngs"]].apply(lambda x:(1-2*x["poisson rate"])/(x["youngs"]),axis=1)
df['stiffness']=df[["flexibility"]].apply(lambda x:(1/x["flexibility"]),axis=1)
df.to_csv('%s/prediction_result.csv'%p6)
df.rename(columns={'Tensile Strength, Ultimate predicted':'U','Tensile Strength, Yield predicted':'Y','Elongation at Break predicted':'El','elasticity.K_VRH predicted':'K_VRH','elasticity.G_VRH predicted':'G_VRH','youngs':'E'},inplace=True)
df['x3']=df[['E','Y']].apply(lambda x:((x['Y']/x['E'])+0.2),axis=1)
df['x0']=df[['x3']].apply(lambda x:((x['x3']+0.2)),axis=1)
df['x2']=df[['E','Y','El']].apply(lambda x:((x['Y']/x['E'])+x['El']),axis=1)
df['x1']=df[['x0','x2']].apply(lambda x:((x['x0']+x['x2'])/2),axis=1)
df['a']=df[['x0','x1','x2','Y','U']].apply(lambda x:(((x['Y']-x['U'])*(x['x2']-x['x0']))/(((x['x2']*x['x2'])-(x['x0'])*x['x2']-(x['x1']*x['x2'])+(x['x1']*x['x0']))*(x['x1']-x['x0']))),axis=1)
df['b']=df[['x0','x1','a','Y','U']].apply(lambda x:((x['U']-x['Y']+(x['a']*x['x0']*x['x0'])-(x['a']*x['x1']*x['x1']))/(x['x1']-x['x0'])),axis=1)
df['c']=df[['b','x0','a','Y']].apply(lambda x:((x['Y']-(x['b']*x['x0'])-x['a']*x['x0']*x['x0'])),axis=1)
df=df[['id','E','U','Y','El','x0','x2','x1','a','b','c','x3','K_VRH','G_VRH','poisson rate','flexibility','stiffness']]
for i in range(0,len(df)-1):
	if df.iat[i,2]>=df.iat[i,3]:
		x=np.arange(df.iat[i,5],df.iat[i,6],0.01)
		y=(df.iat[i,8])*x**2+(df.iat[i,9])*x+df.iat[i,10]
	else:
		x=np.arange(df.iat[i,5],df.iat[i,6],0.01)
		y=df.iat[i,3]+x*0
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
	if df.iat[i,2]>=df.iat[i,3]:
		plt.plot(df.iat[i,7], df.iat[i,2], '.y')
		plt.annotate('Tensile Strength,Ultimate', xy=(df.iat[i,7], df.iat[i,2]), xytext=(df.iat[i,7]+2, df.iat[i,2]), arrowprops=dict(arrowstyle='->'))
		plt.annotate('(%s , %s)'%(df.iat[i,7],df.iat[i,2]), xy=(df.iat[i,7], df.iat[i,2]), xytext=(df.iat[i,7]-1, df.iat[i,2]-50))
	else:
		plt.plot(df.iat[i,7], df.iat[i,3], '.y')
		plt.annotate('Tensile Strength,Ultimate', xy=(df.iat[i,7], df.iat[i,3]), xytext=(df.iat[i,7]+2, df.iat[i,3]), arrowprops=dict(arrowstyle='->'))
		plt.annotate('(%s , %s)'%(df.iat[i,7],df.iat[i,3]), xy=(df.iat[i,7], df.iat[i,3]), xytext=(df.iat[i,7]-1, df.iat[i,3]-50))
	plt.plot(df.iat[i,4],0, '.y')
	plt.annotate('Elongation at break', xy=(df.iat[i,4], 0), xytext=(df.iat[i,6]-1, 50), arrowprops=dict(arrowstyle='->'))
	plt.annotate('(%s , 0)'%df.iat[i,4], xy=(df.iat[i,4], 0), xytext=(df.iat[i,4]-1, 20))
	plt.savefig('%s/%s.png'%(p6,df.iat[i,0]),bbox_inches='tight')
	print('%s finished'%df.iat[i,0])
os.startfile('%s'%p6)

