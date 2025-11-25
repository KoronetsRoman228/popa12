import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask
from tqdm import tqdm
from bs4 import BeautifulSoup
from PIL import Image
import scipy

# Використати 5 з них в try-блоках (numpy, pandas, requests, matplotlib, seaborn)
# 1. numpy
try:
    arr = np.array([1, 2, 3])
    print("Numpy sum:", np.sum(arr))
except Exception as e:
    print("Error using numpy:", e)

# 2. pandas
try:
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    print("Pandas head:\n", df.head())
except Exception as e:
    print("Error using pandas:", e)

# 3. requests
try:
    r = requests.get('https://httpbin.org/get')
    print("Requests status code:", r.status_code)
except Exception as e:
    print("Error using requests:", e)

# 4. matplotlib
try:
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Matplotlib Plot")
    plt.savefig("matplot.png")
    plt.close()
    print("Matplotlib plot saved as matplot.png")
except Exception as e:
    print("Error using matplotlib:", e)

# 5. seaborn
try:
    data = sns.load_dataset("iris")
    sns_plot = sns.pairplot(data, hue="species")
    sns_plot.savefig("seaborn_pairplot.png")
    print("Seaborn pairplot saved as seaborn_pairplot.png")
except Exception as e:
    print("Error using seaborn:", e)
