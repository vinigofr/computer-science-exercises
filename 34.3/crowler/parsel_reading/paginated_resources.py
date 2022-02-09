import time
import requests
from parsel import Selector
import timeit
import json

BASE_URL = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html?'

extrected_content = []

start = timeit.default_timer()
try:
    while next_page_url:
        print("Current URL: ",BASE_URL + next_page_url)
        response = requests.get(BASE_URL + next_page_url) # URL base

        selector = Selector(text=response.text) # Conteudo da pagina
        titles = selector.css(".product_pod h3 a::attr(title)").getall() 
        prices = selector.css(".product_price .price_color::text").getall()
        next_page_url = selector.css(".next a").get() #page-x.html
        next_page_url = selector.css(".next a::attr(href)").get()

        extrected_content.extend(list(zip(titles, prices))) 
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Aplicacao interrompida pelo usuario")

to_json = []

for content in extrected_content:
    to_json.append({
      "title": content[0],
      "price": content[1]
    })

with open('allBooks.json', 'w') as books:
    json.dump(to_json, books)
stop = timeit.default_timer()

print('Tarefa concluida em', round(stop - start) , 'segundos')