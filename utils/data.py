import pandas as pd
from settings import *

# 根据sheet, 获取excel数据
def get_data(sheet_name):
    dataset = pd.read_excel(data_path, sheet_name=sheet_name)
    return dataset.values