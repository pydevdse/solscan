import json
import requests
from get_headers import get_headers


proxy = {"http":"http://brd-customer-hl_2e9cdd80-zone-isp_proxy1:doiu6m99dezi@brd.superproxy.io:33335",
        "https":"http://brd-customer-hl_2e9cdd80-zone-isp_proxy1:doiu6m99dezi@brd.superproxy.io:33335"}

def main(token):
    # url = "https://api-v2.solscan.io/v2/token/transfer?address=4GvsP1a1jknAjZVwdoCq5ShLGxrVyTgwHneSKYPigUgX&page=2&page_size=10&remove_spam=false&exclude_amount_zero=true"
    url = f"https://api-v2.solscan.io/v2/account?address={token}"
    url = "https://api.myip.com/"
    headers = get_headers("headers.txt")
    
    response = requests.get(url, proxies=proxy, headers=headers)
    print(response)
    print(response.json())
    return
    with open(f"{token}.json", "w") as f:
        json.dump(response.json(), f, indent=4, ensure_ascii=False)
    
    
if __name__ == '__main__':
    token = "4GvsP1a1jknAjZVwdoCq5ShLGxrVyTgwHneSKYPigUgX"
    # token = "DLBApwsGc7L3y5821tkU4QSvG7VtR3XGPW4BQb8gmoon"
    main(token)
