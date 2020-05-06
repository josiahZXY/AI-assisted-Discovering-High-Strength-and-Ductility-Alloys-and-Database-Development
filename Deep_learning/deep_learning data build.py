#this is to build a database for cnn to use
import pandas as pd
from pymatgen import Structure
from pymatgen import MPRester
import matplotlib.pyplot as plt
api_key = 'x3NlvC67Z9tPykwGz'
mpr = MPRester(api_key)
df=pd.read_excel(r'D:\FYP_files\database\data_after_processing\CGCNN_bulkmodulus_traindata.xlsx')#this is how to get the cif files
for i in range(0,13110): #this is the number of data in 2019/12/1, there must be more datas
    structure = mpr.get_structure_by_material_id("%s"%df.iat[i,0])
    structure.to("cif","D:/FYP_files/Deep_learning/cgcnn-master/data/example/%s.cif"%df.iat[i,0]) 
    print(i)    
# python main.py --train-ratio 0.6 --val-ratio 0.2 --test-ratio 0.2 data/sample-regression
# python predict.py pre-trained/formation-energy-per-atom.pth.tar data/sample-regression 
#python init.py --idx 2






 
