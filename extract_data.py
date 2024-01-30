import requests
import pandas as pd 
import json 
from concurrent.futures import ThreadPoolExecutor

COLUMNS_LIST = ["id",
                "name",
                "height",
                "weight",
                "base_experience", 
                "order"
                ]

def fetch_data(index):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}')   
    res = res.json() 
    dic = {x: res[x] for x in COLUMNS_LIST}
    df = pd.DataFrame.from_dict(dic,  orient='index')
    return df


def extract_data():
    data_list = []
    with ThreadPoolExecutor(max_workers=5) as executor: 
        futures = [executor.submit(fetch_data, i) for i in range(1, 152)] 
        for future in futures:
            data_list.append(future.result())
    return data_list


pokemon_dt = extract_data()

