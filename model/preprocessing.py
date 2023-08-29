# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:47:31 2023

@author: user
"""

import pandas as pd

row_data = pd.read_csv('C:/Users/user/Desktop/competition/Train_dataset/merged_data_2012_to_2020.csv')

data = row_data.copy()
data.head()
data.info()

seoul = data.loc[(data['STN(ID)']==108), ]
seoul.reset_index(drop=True, inplace=True)
seoul.columns
seoul.to_csv('C:/Users/user/Desktop/competition/data/seoul.csv', index=False)

wonju = data.loc[(data['STN(ID)']==114), ]
wonju.reset_index(drop=True, inplace=True)
wonju.to_csv('C:/Users/user/Desktop/competition/data/wonju.csv', index=False)


eastsea = data.loc[(data['STN(ID)']==106), ]
eastsea.reset_index(drop=True, inplace=True)
eastsea.to_csv('C:/Users/user/Desktop/competition/data/eastsea.csv', index=False)

daejeon = data.loc[(data['STN(ID)']==133), ]
daejeon.reset_index(drop=True, inplace=True)
daejeon.to_csv('C:/Users/user/Desktop/competition/data/daejeon.csv', index=False)

andong = data.loc[(data['STN(ID)']==136), ]
andong.reset_index(drop=True, inplace=True)
andong.to_csv('C:/Users/user/Desktop/competition/data/andong.csv', index=False)

jeonju = data.loc[(data['STN(ID)']==146), ]
jeonju.reset_index(drop=True, inplace=True)
jeonju.to_csv('C:/Users/user/Desktop/competition/data/jeonju.csv', index=False)

daegu = data.loc[(data['STN(ID)']==143), ]
daegu.reset_index(drop=True, inplace=True)
daegu.to_csv('C:/Users/user/Desktop/competition/data/daegu.csv', index=False)

gwangju = data.loc[(data['STN(ID)']==156), ]
gwangju.reset_index(drop=True, inplace=True)
gwangju.to_csv('C:/Users/user/Desktop/competition/data/gwangju.csv', index=False)

busan = data.loc[(data['STN(ID)']==159), ]
busan.reset_index(drop=True, inplace=True)
busan.to_csv('C:/Users/user/Desktop/competition/data/busan.csv', index=False)

yeosu = data.loc[(data['STN(ID)']==168), ]
yeosu.reset_index(drop=True, inplace=True)
yeosu.to_csv('C:/Users/user/Desktop/competition/data/yeosu.csv', index=False)