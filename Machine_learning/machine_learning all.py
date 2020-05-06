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
from matminer.utils.data import PymatgenData
from pymatgen import Composition
mpr=MPDataRetrieval()

api_key = 'x3NlvC67Z9tPykwGz'   
# Set your MP API key here. 
mpr = MPDataRetrieval(api_key)  
mpdr=MPDataRetrieval(api_key)
# df = mpdr.get_dataframe({"elasticity": {"$exists": True}, "elasticity.warnings": []},
                        # ['pretty_formula', 'elasticity.K_VRH', 'elasticity.G_VRH']) 
criteria = {'elasticity.K_VRH': {'$ne': None}}
properties = ['pretty_formula', 'spacegroup.symbol', 'elasticity.K_VRH', 'elasticity.G_VRH','formation_energy_per_atom', 'band_gap',
              'e_above_hull', 'density', 'volume', 'nsites']
df = mpr.get_dataframe(criteria=criteria, properties=properties)
df1=pd.read_csv(r'D:\FYP_files\database\data_after_processing\huizong\huizong.csv')
df=df.reset_index()
df=pd.merge(df,df1)
df=df.set_index("material_id")
df = df[df['elasticity.K_VRH'] > 0]
df = df[df['e_above_hull'] < 0.1]  
df['vpa'] = df['volume']/df['nsites']        
df['poisson_ratio']=df[["elasticity.K_VRH","elasticity.G_VRH"]].apply(lambda x:(3*x["elasticity.K_VRH"]-2*x["elasticity.G_VRH"])/(6*x["elasticity.K_VRH"]+2*x["elasticity.G_VRH"]),axis=1)
from matminer.featurizers.conversions import StrToComposition
df = StrToComposition().featurize_dataframe(df, "pretty_formula")
from matminer.featurizers.composition import ElementProperty
ep_feat = ElementProperty.from_preset(preset_name="magpie")
df = ep_feat.featurize_dataframe(df, col_id="composition")  # input the "composition" column to the featurizer
from matminer.featurizers.conversions import CompositionToOxidComposition
from matminer.featurizers.composition import OxidationStates
df = CompositionToOxidComposition().featurize_dataframe(df, "composition")
os_feat = OxidationStates()
df = os_feat.featurize_dataframe(df, "composition_oxid")
dataset = PymatgenData()
descriptors = ['row', 'group', 'atomic_mass',
               'atomic_radius', 'boiling_point', 'melting_point', 'X']
stats = ["mean", "std_dev"]
ep = ElementProperty(data_source=dataset, features=descriptors, stats=stats)
df = ep.featurize_dataframe(df, "composition")
#Remove NaN values
df = df.dropna()

#y = df['elasticity.K_VRH'].values
y=df['Tensile Strength, Yield'].values
excluded = ["elasticity.G_VRH", "elasticity.K_VRH",  "pretty_formula", 'volume','nsites','spacegroup.symbol','e_above_hull','Tensile Strength, Yield','Elongation at Break ','Tensile Strength,Ultimate',
            "poisson_ratio", "composition", "composition_oxid"]#"elastic_anisotropy"
X = df.drop(excluded, axis=1)
print("There are {} possible descriptors:\n\n{}".format(X.shape[1], X.columns.values))
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
lr = LinearRegression()
lr.fit(X, y)
# get fit statistics
print('training R2 = ' + str(round(lr.score(X, y), 3)))
print('training RMSE = %.3f' % np.sqrt(mean_squared_error(y_true=y, y_pred=lr.predict(X))))
from sklearn.model_selection import KFold, cross_val_score
crossvalidation = KFold(n_splits=10, shuffle=False, random_state=1)
scores = cross_val_score(lr, X, y, scoring='neg_mean_squared_error', cv=crossvalidation, n_jobs=1)
rmse_scores = [np.sqrt(abs(s)) for s in scores]
r2_scores = cross_val_score(lr, X, y, scoring='r2', cv=crossvalidation, n_jobs=1)
print('Cross-validation results:')
print('Folds: %i, mean R2: %.3f' % (len(scores), np.mean(np.abs(r2_scores))))
print('Folds: %i, mean RMSE: %.3f' % (len(scores), np.mean(np.abs(rmse_scores))))
from matminer.figrecipes.plot import PlotlyFig
from sklearn.model_selection import cross_val_predict

pf = PlotlyFig(x_title='DFT (MP) bulk modulus (GPa)',
               y_title='Predicted bulk modulus (GPa)',
               title='Linear regression',
               filename="E:/lr_regression.html")

pf.xy(xy_pairs=[(y, cross_val_predict(lr, X, y, cv=crossvalidation)), ([0, 400], [0, 400])], 
      labels=df['pretty_formula'], 
      modes=['markers', 'lines'],
      lines=[{}, {'color': 'black', 'dash': 'dash'}], 
      showlegends=False
     )
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100, random_state=1)
rf.fit(X, y)
print('training R2 = ' + str(round(rf.score(X, y), 3)))
print('training RMSE = %.3f' % np.sqrt(mean_squared_error(y_true=y, y_pred=rf.predict(X))))
r2_scores = cross_val_score(rf, X, y, scoring='r2', cv=crossvalidation, n_jobs=-1)
scores = cross_val_score(rf, X, y, scoring='neg_mean_squared_error', cv=crossvalidation, n_jobs=-1)
rmse_scores = [np.sqrt(abs(s)) for s in scores]

print('Cross-validation results:')
print('Folds: %i, mean R2: %.3f' % (len(scores), np.mean(np.abs(r2_scores))))
print('Folds: %i, mean RMSE: %.3f' % (len(scores), np.mean(np.abs(rmse_scores))))
from matminer.figrecipes.plot import PlotlyFig

pf_rf = PlotlyFig(x_title='DFT (MP) bulk modulus (GPa)',
                  y_title='Random forest bulk modulus (GPa)',
                  title='Random forest regression',
                  filename="E:/rf_regression.html")

pf_rf.xy([(y, cross_val_predict(rf, X, y, cv=crossvalidation)), ([0, 400], [0, 400])], 
      labels=df['pretty_formula'], modes=['markers', 'lines'],
      lines=[{}, {'color': 'black', 'dash': 'dash'}], showlegends=False)
from sklearn.model_selection import train_test_split
X['pretty_formula'] = df['pretty_formula']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
train_formula = X_train['pretty_formula']
X_train = X_train.drop('pretty_formula', axis=1)
test_formula = X_test['pretty_formula']
X_test = X_test.drop('pretty_formula', axis=1)

rf_reg = RandomForestRegressor(n_estimators=50, random_state=1)
rf_reg.fit(X_train, y_train)
tree0, tree1, tree2 = rf_reg.estimators_[0], rf_reg.estimators_[1], rf_reg.estimators_[2]
# get fit statistics
print('training R2 = ' + str(round(rf_reg.score(X_train, y_train), 3)))
print('training RMSE = %.3f' % np.sqrt(mean_squared_error(y_true=y_train, y_pred=rf_reg.predict(X_train))))
print('test R2 = ' + str(round(rf_reg.score(X_test, y_test), 3)))
print('test RMSE = %.3f' % np.sqrt(mean_squared_error(y_true=y_test, y_pred=rf_reg.predict(X_test))))
from matminer.figrecipes.plot import PlotlyFig
pf_rf = PlotlyFig(x_title='Bulk modulus prediction residual (GPa)',
                  y_title='Probability',
                  title='Random forest regression residuals',
                  filename="E:/rf_regression_residuals.html")

hist_plot = pf_rf.histogram(data=[y_train-rf_reg.predict(X_train), 
                                  y_test-rf_reg.predict(X_test)],
                            histnorm='probability', colors=['blue', 'red'],
                            return_plot=True
                           )
hist_plot["data"][0]['name'] = 'train'
hist_plot["data"][1]['name'] = 'test'
pf_rf.create_plot(hist_plot)
importances = rf.feature_importances_
# included = np.asarray(included)
included = X.columns.values
indices = np.argsort(importances)[::-1]

pf = PlotlyFig(y_title='Importance (%)',
               title='Feature by importances',
               filename='E:/importances.html',
               fontsize=20,
               ticksize=15)

pf.bar(x=included[indices][0:10], y=importances[indices][0:10])
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
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

