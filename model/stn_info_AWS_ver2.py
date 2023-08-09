# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:43:01 2023

@author: user
"""

import pandas as pd

filename = 'C:/Users/user/Desktop/competition/Train_dataset/Train_dataset_part4/Train_dataset_part4/stn_info_AWS.txt'

# 파일을 읽기 모드로 열기
with open(filename, 'r', encoding='UTF8') as file:
    lines = file.readlines()
    
# 데이터를 저장할 빈 리스트 생성
data_list = []

# 20번째 행부터 데이터 추출
for line in lines[19:]:  # 0부터 시작하므로 19는 실제로 20번째 행을 나타냄
    columns = line.strip().split()  # 공백으로 문자열을 분리하여 컬럼 리스트 생성
    data = columns[1]  # 두 번째 열 데이터 추출
    data_list.append(data)  # 추출한 데이터를 리스트에 추가

# 결과 출력
for data in data_list:
    print(data)