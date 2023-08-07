# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:05:07 2023

@author: user
"""

import os
import sys
import glob
import pandas as pd
from netCDF4 import Dataset

import netCDF4 as nc

import numpy as np
import seaborn as sns
import geopandas as pgd
import matplotlib.pyplot as plt



# 파일 인포 조회
path = 'C:/Users/user/Downloads/샘플데이터'
os.chdir(path)
os.getcwd()

dataset_p = 'RDR_avg1h_128_4km_2020-06-09_22_00_00.nc'
dataset = Dataset(dataset_p)

print(dataset)
print(dataset.variables.keys())
nc_value = dataset.variables.keys()

# 데이터 추출
rain1h = dataset.variables['rain1h'][:]
xlats = dataset.variables['XLAT'][:]
xlons = dataset.variables['XLON'][:]

# 레이더 합성자료 생성 
radar_data = rain1h

# 시간대별 강우량 시각화
num_time_steps = radar_data.shape[0]  # 시간 스텝 개수
for time_step in range(num_time_steps):
    plt.figure()
    plt.imshow(radar_data[time_step, np.newaxis], cmap='Blues', origin='lower',
               extent=[xlons.min(), xlons.max(), xlats.min(), xlats.max()])
    plt.colorbar(label='Rainfall (mm/h)')
    plt.title(f"Time Step: {time_step}")
    plt.xlabel('Longitude (degrees)')
    plt.ylabel('Latitude (degrees)')
    plt.show()
    