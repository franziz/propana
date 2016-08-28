from lib.price_list_engine import Engine
import selenium

if __name__ == "__main__":
	success = False
	while not success:
		try:
			engine = Engine()
			engine.crawl()
			success = True
		except selenium.common.exceptions.TimeoutException:
			pass
