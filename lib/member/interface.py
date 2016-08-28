from ..database import Database
from .          import Member

class MemberInterface:
	def __init__(self):
		pass

	@classmethod
	def get_all(self):
		db     = Database.get_db()
		result = []
		for document in db.members.find({}):
			member = Member(
 				  nama = document["nama"],
				 email = document["email"],
				mark_up = document["mark_up"]
			)
			result.append(member)
		return result