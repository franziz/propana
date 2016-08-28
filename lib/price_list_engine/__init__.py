from selenium   import webdriver
from ..database import Database
from .mapper    import MapperFactory
import random
import json

class Engine:
	def __init__(self):
		pass

	def crawl(self):
		print("[price_list_engine][debug] Connecting to database...")
		db = Database.get_db()
		db.price_list.remove({})

		print("[price_list_engine][debug] Loading page...")
		driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
		driver.set_window_size(1366, 768)
		driver.set_page_load_timeout(random.randint(60,180))
		driver.get("http://www.propanareload.com/hargaretail/")
		print("[price_list_engine][debug] Page loaded!")

		print("[price_list_engine][debug] Crawling...")
		products           = []
		product_containers = driver.find_elements_by_xpath("//div[@class='tablewrapper']")
		for container in product_containers:
			product         = {}
			product_name    = container.find_element_by_xpath(".//tr[@class='head']/td")
			product_name    = product_name.text
			item_containers = container.find_elements_by_xpath(".//tr[@class='td1' or @class='td2']")
			items           = []
			for item_container in item_containers:
				descriptions = item_container.find_elements_by_xpath(".//td")
				if len(descriptions) > 0:
					harga = descriptions[2].text
					harga = harga.replace(",","")
					harga = harga.replace(".","")
					harga = int(harga)		
					item  = {
								      "kode" : descriptions[0].text,
								"keterangan" : descriptions[1].text,
								     "harga" : harga,
								    "status" : descriptions[3].text
							}
					items.append(item)
			product.update({
				     "nama" : product_name.title(),
					"items" : items,
					 "tipe" : "",
				  "provider": ""
			})
			products.append(product)

		# Mapping product name with tipe
		print("[price_list_engine][debug] Mapping Tipe...")
		tipe_mapper = MapperFactory.get_mapper(MapperFactory.TIPE)
		for index, product in enumerate(products):
			products[index].update({
				"tipe" : tipe_mapper.map(based_on=product["nama"])
			})
		# Mapping product name with provider
		print("[price_list_engine][debug] Mapping Provider...")
		provider_mapper = MapperFactory.get_mapper(MapperFactory.PROVIDER)
		for index, product in enumerate(products):
			products[index].update({
				"provider" : provider_mapper.map(based_on=product["nama"])
			})
		db.price_list.insert_many(products)
		driver.close()