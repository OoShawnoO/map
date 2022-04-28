# -*- coding:utf-8 -*-
# ※Author = 胡志达
# ※Time = 2022/3/21 19:53
# ※File Name = poidistance.py
# ※Email = 840831038@qq.com
import re

import requests
import time

stations = []
ls = [i for i in range(100,987)]
count = 0
find_str =re.compile(r"<a id='.*?' href='.*?' target='_blank' title='.*?'><span>.*?</span><em>(.*?)</em></a></li>")
for x in range(len(ls)):
    try:
        if x%100==0 and x!=0:
            time.sleep(20)
        line = "https://bus.mapbar.com/chongqing/xianlu/%dlu/"%ls[x]
        req = requests.get(line)
        ls2 = re.findall(find_str,req.text)
        if len(ls2) == 0:
            continue
        print(ls[x], end="路 ")
        count+=1
        for i in ls2:
            if i not in stations:
                stations.append(i)
            print(i,end=" ")
        print("end\n")
    except:
        print(ls[x])

print("\n")
for i in range(len(stations)):
    print(stations[i],end=" ")
print("\n")
print(len(stations))
print(count)



# dic = {}
# for i in range(10):
#     url="https://restapi.amap.com/v5/place/text?key=65529d3c10a4a90685c57ee06b393155&keywords=%s&types=150700|150702|150704&region=重庆市"%ls[i]
#     req = requests.get(url)
#     try:
#         l = []
#         req = req.json()
#         print(req)
#         print(req["pois"][0]["location"])
#         print(req["pois"][0]["address"])
#         l.append(req["pois"][0]["location"])
#         l.append(req["pois"][0]["address"])
#         dic[string[i]] = l
#     except:
#         print(ls[i])
#
# import json
# with open("./station.txt","a+") as f:
#     for key,value in dic.items():
#         f.write(key+" ")
#         for i in value:
#             f.write(i+" ")
#         f.write(" \n")