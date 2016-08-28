import pymongo

class Database:

	@staticmethod
	def get_db():
		db = pymongo.MongoClient("mongodb://mongo:27017/propana")
		db = db.propana
		return db