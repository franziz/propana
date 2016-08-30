from ..database import Database
from .          import Member

class MemberInterface:
	def __init__(self):
		pass

	@classmethod
	def get_all(self, **kwargs):
		use_condition = False
		if len(kwargs.keys()) > 0: use_condition=True

		condition = {}
		if use_condition:
			condition = {"$and":[{key:value} for key,value in kwargs.items()]}

		db     = Database.get_db()
		result = []
		for document in db.members.find(condition):
			member = Member(
 				  nama = document["nama"],
				 email = document["email"],
				mark_up = document["mark_up"]
			)
			result.append(member)
		return result