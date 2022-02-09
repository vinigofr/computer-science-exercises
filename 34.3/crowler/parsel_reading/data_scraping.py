
import requests
from parsel import Selector

BASE_URL = "http://books.toscrape.com/"

response = requests.get(BASE_URL)
selector = Selector(text=response.text)
# print(selector) # Objeto com conteudo da pagina

titles = selector.css(".product_pod h3 a::attr(title)").getall()
prices = selector.css(".product_price .price_color::text").getall()
merged_content = zip(titles, prices) # Juntam os dois elementos

for content in merged_content:
    print(content) # Imprime as tuplas (title, price)
