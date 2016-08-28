from ..database    import Database
from babel.numbers import format_number
import pandas as pd
import os
import shutil

class Generator:
	def __init__(self):
		pass

	@classmethod
	def clean_directory(self):		
		path = os.path.join(".","price_list")
		print("[price_list_generator][debug] Cleaning %s folder" % path)
		if os.path.isdir(path): shutil.rmtree(path)

	@classmethod
	def generate(self, tipe=None, mark_up="0"):
		assert tipe is not None, "tipe is not defined."

		if type(mark_up) is int:
			mark_up = str(mark_up)

		# Prepare directory
		print("[price_list_generator][debug] Preparing directory...")		
		if not os.path.isdir(os.path.join(".","price_list", mark_up)):			
			os.makedirs(os.path.join(".","price_list", mark_up))
		path = os.path.join(".","price_list",mark_up)

		print("[price_list_generator][debug] Building: %s" % tipe)
		writer    = pd.ExcelWriter(os.path.join(path,"%s.xls" % tipe))
		providers = {}
		db        = Database.get_db()
		for group in db.price_list.find({"tipe":"%s" % tipe}):
			print("[price_list_generator][debug] Making: %s" % group["provider"])
			if group["provider"] not in providers: 
				df = pd.DataFrame(columns=["Kode","Keterangan", "Harga","Status"])
				providers.update({group["provider"]:df})
			for item in group["items"]:
				row = {
					      "Kode" : item["kode"],
					"Keterangan" : item["keterangan"],
					     "Harga" : format_number(item["harga"] + int(mark_up), locale='id_id'),
					    "Status" : item["status"]
				}
				providers[group["provider"]] = providers[group["provider"]].append(row, ignore_index=True)

		print("[price_list_generator][debug] Saving...")
		for key,value in providers.items():
			value.to_excel(writer, key, index=False)
		writer.save()
		print("[price_list_generator][debug] Saved!")