import requests

def make_request(endpoint, params=None):
    base_url = "https://open-api.bingx.com"
    response = requests.get(base_url + endpoint, params=params)
    result = response.json()
    return result

if __name__ == '__main__':
    endpoint = "/openApi/swap/v2/quote/contracts"
    params = {}
    ex_info = make_request(endpoint, params)
    print(ex_info)