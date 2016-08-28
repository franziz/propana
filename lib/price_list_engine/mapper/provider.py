from .mapper import Mapper

class ProviderMapper(Mapper):
	def __init__(self):
		Mapper.__init__(self)

	def map(self, based_on=None):
		Mapper.map(self, based_on)

		provider = self.default
		if "telkomsel" in based_on.lower():
			provider = "TELKOMSEL"
		elif "xl" in based_on.lower() or "axis" in based_on.lower():
			provider = "XL AXIS"
		elif "three" in based_on.lower() or "v-tri" in based_on.lower():
			provider = "THREE"
		elif "smartfren" in based_on.lower():
			provider = "SMARTFREN"
		elif "pln" in based_on.lower():
			provider = "PLN"
		elif "indosat" in based_on.lower():
			provider = "INDOSAT"
		elif "bolt" in based_on.lower():
			provider = "BOLT"
		return provider