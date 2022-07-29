import matplotlib.pyplot as plt
#Introduction and dataset pull data
import pandas as pd
nRowsRead = None 
# purchase_data_exe.csv 
purchase_data = pd.read_csv('/Users/yazminmartinez/Documents/Git/e-commercedata/purchase_data_exe.csv', delimiter=',', nrows = nRowsRead)
purchase_data.dataframeName = purchase_data
nRow, nCol = purchase_data.shape
purchase_data.drop(['Unnamed: 7'], axis=1, inplace=True)
print(f" In this dataset we are looking at {nRow} rows and {nCol} columns for an e-commerce website. Here's a sample:")
#Data sample
print(purchase_data.head())
print(purchase_data.describe())
# Define Rows and Columns
import numpy as np
import matplotlib.pyplot as plt
print(purchase_data.corr())
