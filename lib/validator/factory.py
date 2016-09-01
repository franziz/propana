from .email import EmailValidator

class ValidatorFactory:
	EMAIL = 0

	def __init__(self):
		pass

	@classmethod
	def get_validator(self, validator_name=None):
		assert validator_name is not None, "validator_name is not defined."

		if validator_name == ValidatorFactory.EMAIL:
			return EmailValidator()