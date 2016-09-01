from .            import Validator
from ..exceptions import ValidationError

class EmailValidator(Validator):
	def __init__(self):
		Validator.__init__(self)

	def validate(self, str_email=None):
		Validator.validate(self, str_email)

		# At least memiliki @ dan .com ataupun .co.id setelah adanya @
		if "@" not in str_email:
			raise ValidationError("Format email salah.")
		after_at = str_email[str_email.index("@")+1:]
		if ".com"   not in after_at and \
		   ".co.id" not in after_at and \
		   ".org"   not in after_at:
			raise ValidationError("Format email salah.")
