from ..database   		 import Database
from .exceptions         import DuplicateMember
from ..validator.factory import ValidatorFactory
from ..exceptions        import ValidationError
import pymongo

class Member:
	def __init__(self, **kwargs):
		self.nama               = kwargs.get("nama",None)
		self.email              = kwargs.get("email",None)
		self.mark_up            = kwargs.get("mark_up",0)
		self.receive_price_list = kwargs.get("receive_price_list",False)

	def save(self):
		assert self.nama          is not None, "nama is not defined."
		assert self.email         is not None, "email is not defined."
		assert type(self.mark_up) is int     , "incorrect mark_up data type."

		try:
			email_validator = ValidatorFactory.get_validator(ValidatorFactory.EMAIL)
			email_validator.validate(self.email)

			db = Database.get_db()
			db.members.insert({
				              "nama" : self.nama,
				             "email" : self.email,
				           "mark_up" : self.mark_up,
				"receive_price_list" : self.receive_price_list
			})
		except pymongo.errors.DuplicateKeyError:
			raise DuplicateMember("Email sudah pernah didaftarkan.")
		except ValidationError as validation_error:
			raise validation_error
