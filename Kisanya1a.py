from urllib.parse import urljoin

import requests

from bs4 import BeautifulSoup

from urllib import *


visited_urls = set ()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        pass

    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_al('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
     #   print(urls)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, urls2)
                if keyword in urls_join:
                    print(urls_join)
                    spider_urls(url_join, keyword)
            else :
                pass

