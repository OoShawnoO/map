# -*- coding:utf-8 -*-
# ※Author = 胡志达
# ※Time = 2022/4/11 20:22
# ※File Name = find.py
# ※Email = 840831038@qq.com

# with open('line.txt','r',encoding='utf-8') as f:
#     for i in f.readlines():
#         if i == '\n':
#             continue
#         l = i.split(' ')
#         x = set(l)
#         # if l==l[::-1]:
#         #     print(l[0])
#         if len(l)!= len(x):
#             for j in l:
#                 if l.count(j)!=1 and l[l.index(j)] == l[l.index(j)+1]:
#                     print(l[0],j)
import sklearn.preprocessing
from sklearn import model_selection
import numpy as np

stations = []
with open('station.txt','r',encoding="utf-8") as f:
    for line in f.readlines():
        stations.append(line)
stations = stations[0].split(' ')
# print(stations)

pois = []
dic = {}
max_1 = -1
max_2 = -1
min_1 = 99999.0
min_2 = 99999.0

x = np.array([])
y = np.array([])

with open('station_poi.txt','r') as f:
    for line in f.readlines():
        ls = line.split(' ')
        pois.append(ls[0])
        lx = ls[1].replace("\n", '').split(",")
        lx[0] = float(lx[0])
        x = np.append(x,lx[0],axis=None)
        # if lx[0]>max_1:
        #     max_1 = lx[0]
        # if lx[0]<min_1:
        #     min_1 = lx[0]
        lx[1] = float(lx[1])
        # x.append(lx[0])
        # y.append(lx[1])
        y = np.append(y,lx[1],axis=None)
        # if lx[1] > max_2:
        #     max_2 = lx[1]
        # if lx[1] < min_2:
        #     min_2 = lx[1]
        dic[ls[0]] = tuple(lx)
# print(pois)



scaler = sklearn.preprocessing.StandardScaler()
x = scaler.fit_transform(x.reshape(-1,1))
y = scaler.fit_transform(y.reshape(-1,1))
# scaler = sklearn.preprocessing.MinMaxScaler()
# x = scaler.fit_transform(x.reshape(-1,1))
# y = scaler.fit_transform(y.reshape(-1,1))

np.set_printoptions(threshold=np.inf)

np.set_printoptions(precision=3)

np.set_printoptions(suppress=True)

for i in range(len(x)):
    x[i] = x[i]*10000
    y[i] = y[i]*10000

print(x)
print("/")
print(y)

# print(dic)

# print(x,'\n',y,'\n',max_1,'\n',min_1,'\n',max_2,'\n',min_2)
# mid_x = (max_1+min_1)/2
# mid_y = (max_2+min_2)/2
# standard_x = []
# standrad_y = []
# for item in x:
#     j = (item-min_1)/(max_1-min_1)
#     standard_x.append(j)
# for item in y:
#     j = (item-min_2)/(max_2-min_2)
#     standrad_y.append(j)
#
# print(standard_x)
# print(standrad_y)

