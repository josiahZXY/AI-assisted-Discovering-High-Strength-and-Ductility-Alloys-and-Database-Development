import pandas as pd
from sklearn.model_selection import train_test_split
import sys
import numpy as np
from automatminer import MatPipe
import os
path=sys.argv[1]
option=sys.argv[2]
rpath=sys.argv[3]
df=pd.read_excel('%s'%path,index_col='id')
filename ='D:/FYP_files/Machine_learning/pipeline/p_files/%s'%option
pipe = MatPipe.load(filename)
if __name__ =='__main__':
    df = pipe.predict(df)
if option == 'MatPipe_predict_Ultimate_fourthtime_from_composition.p':
	df.to_csv('%s/Ultimate.csv'%rpath)
elif option == 'MatPipe_predict_Fourthpre_Yield_from_composition.p':
	df.to_csv('%s/Yield.csv'%rpath)
elif option == 'MatPipe_predict_thirdelongation_from_composition.p':
	df.to_csv('%s/Elongation.csv'%rpath)
elif option == 'MatPipe_predict_elsticity.second_K_VRH_from_composition.p':
	df.to_csv('%s/K_VRH.csv'%rpath)
elif option=='MatPipe_predict_finalelasticity.G_VRH_from_composition.p':
	df.to_csv('%s/G_VRH.csv'%rpath)