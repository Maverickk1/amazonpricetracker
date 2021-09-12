import requests
from bs4 import BeautifulSoup
import lxml
#url='https://www.amazon.in/HP-3-3250-Laptop-Windows-15s-gr0012AU/dp/B08T6THSMQ/ref=sr_1_11?dchild=1&pf_rd_i=976419031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=166ae945-0b85-405a-afa5-0710c0a6d2e4&pf_rd_r=PSC4A23TB6EZ969PVAMP&pf_rd_s=merchandised-search-18&qid=1628189375&refinements=p_89%3AHP&s=electronics&sr=1-11'
url='https://www.amazon.in/gp/product/B089MS7D9K/ref=s9_acss_bw_cg_CPACSM20_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=77SKKG0C3ZDJZAKW1B3T&pf_rd_t=101&pf_rd_p=c3fe00ec-35dc-4c81-a495-9c7784e5f8df&pf_rd_i=1389401031'
#url='https://www.amazon.in/Bundled-Spider-Man-GTaSport-Ratchet-3Month/dp/B08FNXXH5J/ref=sr_1_1?dchild=1&keywords=ps4&qid=1628108482&sr=8-1'

def get_link_data(url):
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                "Accept-Language":"en",

            }
            r=requests.get(url,headers=headers)

            soup=BeautifulSoup(r.text,'lxml')


            name=soup.select_one(selector="#productTitle").getText()

            name=name.strip()


            price=soup.select_one(selector="#priceblock_ourprice").getText()
            price=float(price[1:].replace(',',""))

            return name,price

print(get_link_data(url))


