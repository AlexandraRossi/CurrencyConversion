import requests
from typing import List, Dict


API_KEY =  "a7e998c78d3fc8d01e04"
SERVER = "https://free.currconv.com"

COUNTRIES_ENDPOINT = SERVER + "/api/v7/countries"
CONVERSION_ENDPOINT = SERVER + "/api/v7/convert"

class ingester:
    def get_countries(self) -> List[Dict]:
        response = requests.get(COUNTRIES_ENDPOINT, params={'apiKey':API_KEY})
        results = []
        if response.status_code == 200:
            json_response = response.json()
            results = [country_dict for country_dict in json_response["results"].values()]
        return results

    def get_conversion_rate(self, source_currency_id, target_currency_id) -> List[Dict]:
        response = requests.get(CONVERSION_ENDPOINT, params={'apiKey': API_KEY})
        result_list = []
        if response.status_code == 200:
            json_response = response.json()
            result_list  = []





        return results


    #def get_conversion_rate(source_currency_id, target_currency_id):
        #response = requests.get(HISTORY_ENDPOINT,
                                #params={'souce_currency_id': source_currency_id, ''},
                                #headers={'Authorization': f'Bearer {API_KEY}',
                                         #'Accept': 'application/json'})

