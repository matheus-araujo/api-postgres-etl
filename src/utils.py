from constants import COLUMNS_LIST, GENERATION
import requests
import pandas as pd 
import numpy as np 
from concurrent.futures import ThreadPoolExecutor

def fetch_data(index):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}').json()
    dic = {x: res[x] for x in COLUMNS_LIST}
    values = np.array(list(dic.values())).reshape(1, 6)
    df = pd.DataFrame((values), columns=list(dic.keys()))
    return df

def transform_data():
    data_list = []
    with ThreadPoolExecutor(max_workers=10) as executor: 
        futures = [executor.submit(fetch_data, i) for i in GENERATION.get("1")] 
        for future in futures:
            data_list.append(future.result())
    df = pd.DataFrame(data_list)
    return df

