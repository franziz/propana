class Mapper:
	def __init__(self):
		self.default = "UNKNOWN"

	def map(self, based_on=None):
		assert based_on is not None, "based_on is not defined."