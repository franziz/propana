from .tipe     import TipeMapper
from .provider import ProviderMapper

class MapperFactory:
	TIPE     = 0
	PROVIDER = 1

	def __init__(self):
		pass

	@classmethod
	def get_mapper(self, mapper_name=None):
		assert mapper_name is not None, "mapper_name is not defined."
		if mapper_name == MapperFactory.TIPE:
			return TipeMapper()
		elif mapper_name == MapperFactory.PROVIDER:
			return ProviderMapper()