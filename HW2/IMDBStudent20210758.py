#!/usr/bin/env python
# coding: utf-8

# In[34]:


import sys 
import re

f1 = open(sys.argv[1], 'rt')
#f1 = open('movies_exp.txt', 'rt') #파라미터로 받은 것으로 바꾸기)
index = 0
genre = dict()
tmpList = []

for line in f1:
    index = line.rfind('::')
    tmpLine = line[index+2::].rstrip('\n')
    tmpList = tmpLine.split('|')
   
    for i in tmpList:
        if i not in genre:
            genre[i] = 1
        else:
            genre[i] += 1
            
#print(genre)
    
f2 = open(sys.argv[2], 'wt')
#f2 = open('output.txt', 'wt') #파라미터로 받은 것으로 바꾸기)
for k,v in zip(genre.keys(), genre.values()):
    data = "%s %d\n" % (k, v)
    f2.write(data)
    
f1.close()
f2.close()


# In[ ]:




