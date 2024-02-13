from constants import COLUMNS_LIST, GENERATION
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import create_engine
from pathlib import Path  
import pandas as pd 
import configparser
import requests


def fetch_data(index):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{index}').json()
    dic = {x: res[x] for x in COLUMNS_LIST}
    return dic
  
def transform_data():
    data_list = []
    with ThreadPoolExecutor(max_workers=10) as executor: 
        futures = [executor.submit(fetch_data, i) for i in GENERATION.get("1")] 
        for future in futures:
            data_list.append(future.result())
    df = pd.DataFrame(data_list)
    return df

def extract_to_csv():
    filepath = Path('../data/exctract.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    return transform_data().to_csv(filepath, index=False)

def save_in_db():
    return transform_data().to_sql('pokemons', engine, if_exists='replace', index=False)
