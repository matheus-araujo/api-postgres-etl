import requests
import pandas as pd 
import json 
 
def get_data():
    res = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151&offset=0')
    res = res.json()
    res = res['results']
    df = pd.DataFrame(res, columns=['name','url'])
    return df


print(get_data())
