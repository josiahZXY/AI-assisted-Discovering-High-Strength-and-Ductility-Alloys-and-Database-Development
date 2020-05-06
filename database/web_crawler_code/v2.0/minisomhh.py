
#%%
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import pylab as plt
from matplotlib.patches import Patch

#%%
from sklearn import datasets
iris=datasets.load_iris()
print("data shape:",iris.data.shape)
feature_names=iris.feature_names
class_name=iris.target_names
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#%%
from minisom import MiniSom
# 样本数量
N=X_train.shape[0]
# 维度
M=X_train.shape[1]
#%%
# 设置超参数
from math import ceil
import numpy as np
size=ceil(np.sqrt(5*np.sqrt(N)))
print(f"最佳边长：{size}")
max_iter=200
#%%
som=MiniSom(size,size,M,sigma=3,learning_rate=0.5,neighborhood_function='bubble')
#%%
som.pca_weights_init(X_train)
#%%
som.train_batch(X_train,max_iter,verbose=True)
#%%
winmap=som.labels_map(X_train,y_train)
#%%
np.sum(list(winmap.values()))
#%%
np.sum(list(winmap.values())).most_common()
#%%
som.winner(X_test[0,:])  # win_pos
#%%
def classify(som,data,winmap):
    default_class=np.sum(list(winmap.values())).most_common()[0][0]
    res=[]
    for d in data:
        win_pos=som.winner(d)
        if win_pos in winmap:
            res.append(winmap[win_pos].most_common()[0][0])
        else:
            res.append(default_class)
    return res
#%%
y_pred = classify(som,X_test,winmap)
#%%
print(classification_report(y_test, np.array(y_pred)))
#%%
heatmap = som.distance_map()  #生成U-Matrix
plt.imshow(heatmap, cmap='bone_r')      #miniSom案例中用的pcolor函数,需要调整坐标
plt.colorbar()
#%%
plt.figure(figsize=(9, 9))
# 背景上画U-Matrix
heatmap = som.distance_map()
plt.pcolor(heatmap, cmap='bone_r')  # plotting the distance map as background

# 定义不同标签的图案标记
markers = ['o', 's', 'D']
colors = ['C0', 'C1', 'C2']
category_color = {'setosa': 'C0',
                  'versicolor': 'C1',
                  'virginica': 'C2'}
for cnt, xx in enumerate(X_train):
    w = som.winner(xx)  # getting the winner
    # 在样本Heat的地方画上标记
    plt.plot(w[0]+.5, w[1]+.5, markers[y_train[cnt]], markerfacecolor='None',
             markeredgecolor=colors[y_train[cnt]], markersize=12, markeredgewidth=2)
plt.axis([0, size, 0, size])
ax = plt.gca()
ax.invert_yaxis() #颠倒y轴方向
legend_elements = [Patch(facecolor=clr,
                         edgecolor='w',
                         label=l) for l, clr in category_color.items()]
plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, .95))
plt.show()
#%%
label_name_map_number = {"setosa":0,"versicolor":1,"virginica":2}

from matplotlib.gridspec import GridSpec
plt.figure(figsize=(9, 9))
the_grid = GridSpec(size, size)
for position in winmap.keys():
    label_fracs = [winmap[position][label] for label in [0,1,2]]
    plt.subplot(the_grid[position[1], position[0]], aspect=1)
    patches, texts = plt.pie(label_fracs)
    plt.text(position[0]/100, position[1]/100,  str(len(list(winmap[position].elements()))),
              color='black', fontdict={'weight': 'bold',  'size': 15},
              va='center',ha='center')
plt.legend(patches, class_name, loc='center right', bbox_to_anchor=(-1,9), ncol=3)
plt.show()

#%%
plt.figure(figsize=(10, 10))
for i, f in enumerate(feature_names):
    plt.subplot(3, 3, i+1)
    plt.title(f)
    plt.imshow(W[:,:,i], cmap='coolwarm')
    plt.colorbar()
    plt.xticks(np.arange(size+1))
    plt.yticks(np.arange(size+1))
#plt.tight_layout()
plt.show()
