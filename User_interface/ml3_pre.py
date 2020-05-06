from automatminer import MatPipe
from sklearn.model_selection import train_test_split
import sys
import pandas as pd
import numpy as np
import os
#a=sys.argv[1]
i={'composition':[sys.argv[1]]}
rpath=sys.argv[2]
df=pd.DataFrame(i)
filename ='D:/FYP_files/Machine_learning/pipeline/p_files/MatPipe_predict_thirdelongation_from_composition.p'
#MatPipe_predict_thirdelongation_from_composition.p
#MatPipe_predict_Ultimate_fourthtime_from_composition.p
pipe = MatPipe.load(filename)
if __name__ =='__main__':
    df = pipe.predict(df)
df.to_csv('%s/elongation.csv'%rpath)
