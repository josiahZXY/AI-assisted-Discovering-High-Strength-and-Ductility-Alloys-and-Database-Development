import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_excel(r'D:\AI_Fina_Year_Project\finderror2.xlsx')
del df['id']
del df['name']
df=df.set_index('FYP id')
train_df, test_df = train_test_split(df, test_size=0.1, shuffle=True, random_state=20200420)
target = ""
prediction_df = test_df.drop(columns=[target])
prediction_df.head()
from automatminer import MatPipe
pipe = MatPipe.from_preset("express")
pipe.fit(train_df, target)
prediction_df = pipe.predict(prediction_df)
from sklearn.metrics import mean_absolute_error
dr.fit(train_df["composition"], train_df[target])
true = test_df[target]
matpipe_test = prediction_df[target + " predicted"]
mae_matpipe = mean_absolute_error(true, matpipe_test)
print("MatPipe MAE: {} eV".format(mae_matpipe))