import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'https://music.163.com/#/discover/toplist'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()