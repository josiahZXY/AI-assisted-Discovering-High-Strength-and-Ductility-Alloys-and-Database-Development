#Machine_learning, how to build a basic dataframe
#This is for automatminer
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Set pandas view options
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from sklearn.model_selection import train_test_split
from automatminer import MatPipe
from matminer.data_retrieval.retrieve_MP import MPDataRetrieval
# mpr=MPDataRetrieval()
# mpdr=MPDataRetrieval()
api_key = 'x3NlvC67Z9tPykwGz'   
# Set your MP API key here. 
mpr = MPDataRetrieval(api_key) 
# api_key = None   # Set your MP API key here. 
# mpr = MPDataRetrieval(api_key)  
df = mpr.get_dataframe({"elasticity": {"$exists": True}, "elasticity.warnings": []},
                        ['pretty_formula', 'elasticity.K_VRH', 'elasticity.G_VRH'])   
#/ criteria = {'elasticity.K_VRH': {'$ne': None}}
#/ properties = ['pretty_formula', 'elasticity.K_VRH', 'elasticity.G_VRH']
# get the data
# df=mpr.get_dataframe(criteria=criteria, properties=properties)
# Filter out unstable entries and negative bulk moduli
df=df[df['elasticity.K_VRH'] > 0]
df=df[df['elasticity.G_VRH'] > 0]
from matminer.featurizers.composition import ElementProperty
from pymatgen import Composition
df["composition"] = df['pretty_formula'].map(lambda x: Composition(x))
df = df.dropna()
del df['pretty_formula']
df.to_csv('C:/Users/DELL/Documents/basicdata.csv')#the file position must be changed as everyone get different store position
#first, we need to predict the elasticity.K_VRH
del df['elasticity.G_VRH']
df["composition"].unique().shape[0]
train_df, test_df = train_test_split(df, test_size=0.15, shuffle=True, random_state=20191201)
target = "elasticity.K_VRH"
prediction_df = test_df.drop(columns=[target])
prediction_df.head()#show the basicdata of prediction to see if there are some errors
prediction_df.describe()
pipe = MatPipe.from_preset("express")#the heavy can change to express or light, judge on how exactly the data you want to get
pipe.fit(train_df, target)#this will take a long time
prediction_df = pipe.predict(prediction_df)
prediction_df.to_csv('C:/Users/DELL/Documents/predictionK_VRH.csv')
from sklearn.metrics import mean_absolute_error
from sklearn.dummy import DummyRegressor
# fit the dummy
dr = DummyRegressor()
dr.fit(train_df["composition"], train_df[target])
dummy_test = dr.predict(test_df["composition"])
# Score dummy and MatPipe
true = test_df[target]
matpipe_test = prediction_df[target + " predicted"]
mae_matpipe = mean_absolute_error(true, matpipe_test)
mae_dummy = mean_absolute_error(true, dummy_test)
print("K_VRH Dummy MAE: {} ".format(mae_dummy))
print("K_VRH MatPipe MAE: {} ".format(mae_matpipe))
filename = "C:/Users/DELL/Documents/MatPipe_predict_elsticity.K_VRH_from_composition.p"
pipe.save(filename) #save the pipeline in order to use in the future
summary = pipe.summarize(filename="C:/Users/DELL/Documents/MatPipe_predict_elsticity.K_VRH_from_composition_summary.json")
df=pd.read_csv('C:/Users/DELL/Documents/basicdata.csv',index_col='material_id')
del df['elasticity.K_VRH']
df["composition"].unique().shape[0]
train_df, test_df = train_test_split(df, test_size=0.15, shuffle=True, random_state=20191202)
target = "elasticity.G_VRH"
prediction_df = test_df.drop(columns=[target])
prediction_df.head()#show the basicdata of prediction to see if there are some errors
prediction_df.describe()
pipe = MatPipe.from_preset("express")#the heavy can change to express or light, judge on how exactly the data you want to get
pipe.fit(train_df, target)#this will take a long time
prediction_df = pipe.predict(prediction_df)
prediction_df.to_csv('C:/Users/DELL/Documents/predictionG_VRH.csv')
# fit the dummy
dr = DummyRegressor()
dr.fit(train_df["composition"], train_df[target])
dummy_test = dr.predict(test_df["composition"])
# Score dummy and MatPipe
true = test_df[target]
matpipe_test = prediction_df[target + " predicted"]
mae_matpipe = mean_absolute_error(true, matpipe_test)
mae_dummy = mean_absolute_error(true, dummy_test)
print("G_VRH Dummy MAE: {} ".format(mae_dummy))
print("G_VRH MatPipe MAE: {} ".format(mae_matpipe))
filename = "C:/Users/DELL/Documents/MatPipe_predict_elsticity.G_VRH_from_composition.p"
pipe.save(filename) #save the pipeline in order to use in the future
summary = pipe.summarize(filename="C:/Users/DELL/Documents/MatPipe_predict_elsticity.G_VRH_from_composition_summary.json")
# now we have double predictions data: predictionK_VRH and predictionG_VRH
df1=pd.read_csv('C:/Users/DELL/Documents/predictionK_VRH.csv')
df1=pd.DataFrame(df1,columns=['material_id','elasticity.K_VRH predicted'])
df2=pd.read_csv('C:/Users/DELL/Documents/predictionG_VRH.csv')
df2=pd.DataFrame(df2,columns=['material_id','elasticity.G_VRH predicted'])
df3=pd.merge(df1,df2)
#df3["young's"]=data[["elasticity.K_VRH predicted","elasticity.G_VRH predicted"]].apply(lambda x:x["a"]+x["b"],axis=1)
df3['youngs module']=df3[["elasticity.K_VRH predicted","elasticity.G_VRH predicted"]].apply(lambda x:(9*x["elasticity.K_VRH predicted"]*x["elasticity.G_VRH predicted"])/(3*x["elasticity.K_VRH predicted"]+x["elasticity.G_VRH predicted"]),axis=1)
df3['poisson rate']=df3[["elasticity.K_VRH predicted","youngs module"]].apply(lambda x:(3*x["elasticity.K_VRH predicted"]-x["youngs module"])/(6*x["elasticity.K_VRH predicted"]),axis=1)
df3['flexibility']=df3[["poisson rate","youngs module"]].apply(lambda x:(1-2*x["poisson rate"])/(x["youngs module"]),axis=1)
df3['stiffness']=df3[["flexibility"]].apply(lambda x:(1/x["flexibility"]),axis=1)
df3['good']=df3[["elasticity.K_VRH predicted","elasticity.G_VRH predicted"]].apply(lambda x: (1*x["elasticity.K_VRH predicted"])/(1*x["elasticity.G_VRH predicted"]),axis=1)
df3=df3.sort_values(by='stiffness',ascending=True)
df3.to_csv('C:/Users/DELL/Documents/prediction.csv')
print("Machine_learning done!")
#machine_learning done!
#Then let's plot and see how exactly the prediction is
df=pd.read_csv('C:/Users/DELL/Documents/predictionK_VRH.csv')
df=pd.DataFrame(df,columns=['material_id','elasticity.K_VRH predicted'])
df1=pd.read_csv('C:/Users/DELL/Documents/basicdata.csv')
df1=pd.DataFrame(df1,columns=['material_id','elasticity.K_VRH'])
df2=pd.merge(df,df1)
df2=df2.sort_values(by='elasticity.K_VRH',ascending=True)
df2.to_csv('C:/Users/DELL/Documents/comparisionK_VRH.csv')
df3=pd.read_csv('C:/Users/DELL/Documents/predictionG_VRH.csv')
df3=pd.DataFrame(df3,columns=['material_id','elasticity.G_VRH predicted'])
df4=pd.read_csv('C:/Users/DELL/Documents/basicdata.csv')
df4=pd.DataFrame(df4,columns=['material_id','elasticity.G_VRH'])
df5=pd.merge(df3,df4)
df5=df5.sort_values(by='elasticity.G_VRH',ascending=True)
df5.to_csv('C:/Users/DELL/Documents/comparisionG_VRH.csv')
y1=df2['elasticity.K_VRH predicted']
y2=df2['elasticity.K_VRH']
x1=df2['elasticity.K_VRH']
y3=df5['elasticity.G_VRH predicted']
y4=df5['elasticity.G_VRH']
x2=df5['elasticity.G_VRH']
plt.figure()
plt.scatter(x1,y1)
plt.plot(x1,y2)
plt.xlabel("normal K_VRH")
plt.ylabel("predicted K_VRH")
plt.title("comparisionK")
plt.figure()
plt.scatter(x2,y3)
plt.plot(x2,y4)
plt.xlabel("normal G_VRH")
plt.ylabel("predicted G_VRH")
plt.title("comparisionG")
plt.show()




