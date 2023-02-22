import json
import os
from pyecharts import options as opts
from pyecharts.charts import Graph
import pandas as pd
import numpy as np

df = pd.read_csv("matrix2.csv")
print(df)
k = 0
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if np.isnan(df.values[i][j]) == False:
            print("{\"id\": \"" + str(k) + "\", \"source\": \"" + str(i) + "\", \"target\": \"" + str(j) + "\"},")
            k += 1