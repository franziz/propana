import requests
import os

class Mailgun:
	API  = "key-6e54b71b5f7df055caa212e2ce85cf13"
	BASE = "https://api.mailgun.net/v3/syuping.com"

	def __init__(self, **kwargs):
		self._cc         = kwargs.get("cc",None)
		self._bcc        = kwargs.get("bcc",None)
		self._subject    = kwargs.get("subject",None)
		self._text       = kwargs.get("text",None)
		self._html       = kwargs.get("html",None)
		self._attachment = kwargs.get("attachment",None)
		self._recipients = kwargs.get("recipients",None)
		self._sender     = kwargs.get("sender",None)


	def generate_data(self):
		assert self._recipients is not None, "recipients is not defined."
		assert self._sender     is not None, "sender is not defined."
		assert self._subject    is not None, "subject is not defined."
		assert self._text       is not None, "text is not defined." 

		data = {
			 "to" : self._recipients,
			"from": self._sender
		}
		if self._cc        is not None: data.update({"cc":self._cc})
		if self._bcc       is not None: data.update({"bcc":self._bcc})
		if self._subject   is not None: data.update({"subject":self._subject})
		if self._text      is not None: data.update({"text":self._text})
		if self._html      is not None: data.update({"html":self._html})
		return data

	def add_attachment(self, file_path=None):
		if not os.path.isfile(file_path): raise TypeError("File bukan sebuah File.")
		if self._attachment is None: self._attachment = []
		self._attachment.append(("attachment", open(file_path, "rb")))

	def add_recipient(self, name=None, address=None):
		assert address is not None, "address is not defined."
		assert name    is not None, "name is not defined."
		if self._recipients is None: self._recipients = []
		self._recipients.append("%s <%s>" % (name, address))

	def set_sender(self, name=None, address=None):
		assert address is not None, "address is not defined."
		assert name    is not None, "name is not defined."
		self._sender = "%s <%s>" % (name, address)

	def send(self, **kwargs):
		self._text    = kwargs.get("text", self._text)
		self._html    = kwargs.get("html", self._html)
		self._subject = kwargs.get("subject", self._subject)

		if self._attachment is None:
			self._attachment = []
		assert type(self._attachment) is list, "incorrect attachment data type."

		return requests.post(
			  url = "%s/messages" % Mailgun.BASE,
			 auth = ("api", Mailgun.API),
			files = self._attachment,
			 data = self.generate_data()
		)