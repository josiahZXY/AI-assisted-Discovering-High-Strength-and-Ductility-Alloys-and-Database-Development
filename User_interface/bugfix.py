import os

a1='cd C:/Users/zhang/cgcnn-master && python C:/Users/zhang/cgcnn-master/predict.py C:/Users/zhang/cgcnn-master/pre-trained/elongation_best.pth.tar C:/Users/zhang/cgcnn-master/data/elongation'
#格式为a='cd C:/Users/shouw/cgcnn-master && python predict.py pre-trained/Ultimate.pth.tar C:/Users/shouw/mt-cgcnn-master/data/ts_Ultimate'


d=os.system(a1)
print(a1)
print(d)
