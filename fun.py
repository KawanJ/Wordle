#%%
import pandas as pd
import numpy as np

df = np.array(pd.read_csv("wordle.csv"), dtype=str)
#%%
dict1 = {}
for i in df:
    for j in i[0]:
        if j in dict1:
            dict1[j] += 1
        else:
            dict1[j] = 1
#%%
def nextword(y,yellow,g,green,ignore):
    ig = 'T'
    while(ig !='F'):
        ig = input("Enter letter to ignore: ")
        if ig =="F":
            break
        ignore.append(ig)  
    temp = []
    for i in df:
        yel = yellow.copy()
        gre = green.copy()
        c = 0
        b = 0
        remo = 0
        for z in gre:
            if i[0][int(z[1])] == z[0]:
                b+=1
        for z in yel:
            if i[0][int(z[1])] == z[0]:
                remo=1
        for j in i[0]:
            for u in ignore:
                if j==u:
                    remo=1
            for k in yel:
                if j==k[0]:
                    c+=1
                    yel.remove(k)
        if c==y and g==b and remo==0:
            temp.append(i[0])
    print(temp)
    max = 0
    word = ''
    for i in temp:
        tmp=0
        for j in i:
            tmp+=dict1[j]
        if tmp>max:
            max = tmp
            word = i
            print(max,word)           
    print("Best Word: " + word)
    y = int(input("Enter number of yellows: "))
    yellow = []
    for i in range(y):
        tmp = input()
        yellow.append(tmp)
    g = int(input("Enter number of greens: "))
    green = []
    for i in range(g):
        tmp = input()
        green.append(tmp)
    nextword(y,yellow , g, green,ignore)
    
    
def start():        
    y = int(input("Enter number of yellows: "))
    yellow = []
    for i in range(y):
        tmp = input()
        yellow.append(tmp)
    g = int(input("Enter number of greens: "))
    green = []
    for i in range(g):
        tmp = input()
        green.append(tmp)
    nextword(y,yellow , g, green,[])
    
start()
