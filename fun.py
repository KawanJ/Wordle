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
