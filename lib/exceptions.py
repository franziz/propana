class ValidationError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class ConfigNotFound(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindField(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindTemplate(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindFolder(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CannotFindCrawler(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CommandError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InvalidConfigFormat(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InvalidInput(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InvalidDateFormat(BaseException):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class FutureDateError(BaseException):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class CannotOpenURL(BaseException):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class

class PageNotFound(Exception):
	def __init__(self,value):
		self.value = value
	#end def

	def __str__(self):
		return repr(self.value)
	#end def
#end class