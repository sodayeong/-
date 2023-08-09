# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:21:06 2023

@author: user
"""

import pandas as pd

filename = 'C:/Users/user/Desktop/competition/Train_dataset/Train_dataset_part4/Train_dataset_part4/stn_info_AWS.txt'

# 파일을 읽기 모드로 열기
with open(filename, 'r', encoding='UTF8') as file:
    lines = file.readlines()

data_row = []

# 각 줄을 순회하며 공백으로 분할하여 데이터 추출
for line in lines[19:]:
    items = line.split()
    data_row.append(items)
    
columns = ['STN_ID', 'LON', 'LAT', 'STN_SP', 'HT', 'HT_WD', 'LAU', 'STN', 'STN_KO', '*', 'STN_EN', 'FCT_ID', 'LAW_ID', 'BASIN']

# 나머지 행을 데이터로 저장하는 리스트 초기화
data_row = [line.split() for line in lines[20:]]

# 추출된 데이터를 판다스 DataFrame으로 변환
data = pd.DataFrame(data_row, columns = columns)

# data 출력 
data.head()
data.tail() 

data = data.drop(data.index[-1]) # 마지막 행 삭제
data.tail() # 확인

data.info()
data.columns

# object를 수치형으로 변환 
data = data.astype({'STN_ID' : 'int', 
                    'LON' : 'float', 
                    'LAT' : 'float', 
                    'STN_SP' : 'object', 
                    'HT' : 'float', 
                    'HT_WD' : 'float', 
                    'LAU' : 'object',
                    'STN' : 'object', 
                    'STN_KO' : 'str', 
                    '*' : 'object', 
                    'STN_EN' : 'object', 
                    'FCT_ID' : 'object', 
                    'LAW_ID' : 'object', 
                    'BASIN' : 'object'}) # 'null 처리 해야함'
data.info() # 확인 

data['STN_KO'].value_counts() # 722개의 지역

# 학습 데이터 셋 (전체 지점에 대해 학습)

# 예측 대상 지점 추출
# 서울(108), 원주(114), 동해(106), 대전(133), 안동(136), 전주(146), 대구(143), 광주(156), 부산(159), 여수(168), 이상 10개 지점 (괄호는 station ID)
forecast_site = data[(data['STN_ID']==108) | (data['STN_ID']==114) | (data['STN_ID']==106) | (data['STN_ID']==133) | (data['STN_ID']==136) | (data['STN_ID']==146) | (data['STN_ID']==143)  | (data['STN_ID']==156)| (data['STN_ID']==159)  | (data['STN_ID']==168)]
forecast_site.head() # 예측 대상이 없는 지역이 다 섯개 있네;

