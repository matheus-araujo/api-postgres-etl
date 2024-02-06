import requests
import pandas as pd 
import json 
from concurrent.futures import ThreadPoolExecutor

## constants
COLUMNS_LIST = ["id",
                "name",
                "height",
                "weight",
                "base_experience", 
                "order"
                ]
#funtion the will extract the data from API and store in da pandas data frame.
'''
def fetch_data(index):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}')   
    res = res.json() 
    dic = {x: res[x] for x in COLUMNS_LIST}
    #create a better way to save this data frame a correct form;
    df = pd.DataFrame.from_dict(dic,  orient='index')
    return df


def extract_data():
    data_list = []
    with ThreadPoolExecutor(max_workers=5) as executor: 
        futures = [executor.submit(fetch_data, i) for i in range(1, 152)] 
        for future in futures:
            data_list.append(future.result())
    return data_list

'''
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/1').json()
dic = {x: res[x] for x in COLUMNS_LIST}
print(dic)


