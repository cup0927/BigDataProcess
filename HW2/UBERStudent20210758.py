#!/usr/bin/env python
# coding: utf-8

# In[19]:


import sys 
import re
import datetime

f1 = open(sys.argv[1], 'rt')
f2 = open(sys.argv[2], 'wt')
#f1 = open('uber_exp.txt', 'rt') #파라미터로 받은 것으로 바꾸기)
#f2 = open('outputUber.txt', 'wt') #파라미터로 받은 것으로 바꾸기)
tmpList = []
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT','SUN']
regionAndDays = []
tripsAndVehicles = dict()

for line in f1:
    tmpLine = line.rstrip('\n')
    tmpList = tmpLine.split(',')
    vehiclesAndTrips = tmpList[2]+','+ tmpList[3]
    date = tmpList[1].split('/')
    week = days[datetime.date(int(date[2]), int(date[0]), int(date[1])).weekday()]
    regionAndDays = tmpList[0]+','+ week
    
    if regionAndDays not in tripsAndVehicles:
        tripsAndVehicles[regionAndDays] = tmpList[2]+','+ tmpList[3]
    else:
        t, v = map(int, tripsAndVehicles.get(regionAndDays).split(','))
        newT, newV = int(tmpList[2]), int(tmpList[3])
        #print(newT, newV)
        tripsAndVehicles[regionAndDays] = str(t+newT) +','+ str(v+newV)

#     for i in regionAndDays:
#         if i not in tripsAndVehicles:
#             tripsAndVehicles[i] = tmpList[2]+','+ tmpList[3]
#         else:
#             t, v = map(int, tripsAndVehicles.get(i).split(','))
#             newT, newV = int(tmpList[2]), int(tmpList[3])
#             #print(newT, newV)
#             tripsAndVehicles[i] = str(t+newT) +','+ str(v+newV)
    #print(tripsAndVehicles)
    
for k,v in zip(tripsAndVehicles.keys(), tripsAndVehicles.values()):
    data = "%s %s\n" % (k, v)
    f2.write(data)

f1.close()
f2.close()


# In[ ]:




