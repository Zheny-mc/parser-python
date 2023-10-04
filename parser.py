from typing import List

import requests
from bs4 import BeautifulSoup
import re
import time

from models import Product
from work_exel import lst_to_exel

headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2271 Safari/537.36",
    "Accept-Language": "ru,en;q=0.9"
}




def run_request(url, product_name):
    try:
        resp = requests.get(url, headers=headers)
        print(resp.status_code)
        # print(type(resp.text))
        with open(f'{product_name}.html', 'w', encoding='utf-8') as f:
            f.write(resp.text)

    except Exception as e:
        print(e)

def get_info_product(link, text) -> Product:
    soup = BeautifulSoup(text, 'html.parser')
    try:
        title = soup.find('span', {'id': "productTitle"}).text.strip()
        pricing = soup.find("span", {"class": "a-price"})
        pricing = pricing.find("span").text.strip() if pricing else None

        product_description = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini").find_all("span")
        about = ' '.join( [i.text.strip() for i in product_description])

        images = re.findall('"hiRes":"(.+?)"', text)

        return Product(title, pricing, about, link, images)


    except Exception as e:
        print(e)

def get_links(name='Iphone') -> List[Product]:
    run_request(f'https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A281407&ref=nav_em__nav_desktop_sa_intl_accessories_and_supplies_0_2_5_2', 'site')
    with open('site.html', encoding='utf-8') as f:
        text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    lst_titles_product = soup.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal", href=True)
    res = [i["href"] for i in lst_titles_product]
    # print(*res, sep='\n\n')
    return res


def run():
    links = get_links()

    lst_product: List[Product] = []
    for url in links[:20]:
        run_request(f'https://www.amazon.com{url}', 'product')
        with open('product.html', encoding='utf-8') as f:
            text = f.read()
        lst_product.append(get_info_product(f'https://www.amazon.com{url}', text))
        time.sleep(5)

    lst_to_exel(lst_product)

run()


