# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:54:19 2023

@author: user
"""

import pandas as pd

filename = 'C:/Users/user/Desktop/2023 DATA·AI 분석 경진대회/샘플데이터/AWS_hourly_201203010000.txt'

# 파일을 읽기 모드로 열기
with open(filename, 'r') as file:
    lines = file.readlines()

data_row = []

# 각 줄을 순회하며 공백으로 분할하여 데이터 추출
for line in lines:
    items = line.split()
    data_row.append(items)
    
# 첫 번째 행을 컬럼으로 설정
columns = lines[1].split()
columns.remove('#')
print(columns)

# 나머지 행을 데이터로 저장하는 리스트 초기화
data_row = [line.split() for line in lines[3:]]

# 추출된 데이터를 판다스 DataFrame으로 변환
data = pd.DataFrame(data_row, columns = columns)

# data 출력 
data.head()
data.tail() 

data = data.drop(data.index[-1]) # 마지막 행 삭제
data.tail() # 확인

data.columns

# KST 처리
data['YYMMDDHHMI'] = pd.to_datetime(data['YYMMDDHHMI'], format='%Y%m%d%H%M')
print(data)

data['Year'] = data['YYMMDDHHMI'].dt.year
data['Month'] = data['YYMMDDHHMI'].dt.month
data['Day'] = data['YYMMDDHHMI'].dt.day
data['Hour'] = data['YYMMDDHHMI'].dt.hour

data.columns

data = data[['Year', 'Month', 'Day', 'Hour', 'STN', 'TA', 'WD', 'WS', 'RN_DAY', 'RN_HR1', 'HM', 'PA', 'PS']]
print(data.shape)

data.info()
# object를 수치형으로 변환 
data = data.astype({'STN' : 'int', 
                    'TA' : 'float', 
                    'WD' : 'float', 
                    'WS' : 'float', 
                    'RN_DAY' : 'float', 
                    'RN_HR1' : 'float', 
                    'HM' : 'float', 
                    'PA' : 'float', 
                    'PS' : 'float'})
print(data.info()) # 확인 

data['STN'].value_counts(ascending = True) # 697개 STN(ID)


# STN(ID)가 예측하고자 하는 지역일지?
# 각 컬럼명 설명 필요
