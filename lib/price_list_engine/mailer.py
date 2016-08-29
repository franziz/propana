from ..member     import Member
from ..exceptions import CannotFindFolder
from envelopes    import Envelope
import os
import arrow
import glob

class Mailer:
	def __init__(self):
		self.mail_server = "mail_server"
		pass

	def send(self, member=None):
		assert member       is not None, "member is not defined."
		assert type(member) is Member  , "incorrect member data type."
		assert member.nama  is not None, "nama is not defined."
		assert member.email is not None, "email is not defined."

		template_path = os.path.join(".","templates")
		if not os.path.isdir(template_path): raise CannotFindFolder("Cannot find %s folder" % template_path)
		body = open(os.path.join(template_path, "price_list.smet"),"r")
		body = body.read()
		body = body.format(tanggal=arrow.now().date(), nama=member.nama)

		envelope = Envelope(
			from_addr = (u"pricelist@syuping.com", u"Syuping Mobile"),
			to_addr = (u"%s" % member.email, u"%s" % member.nama),
			subject = u"Price List %s" % arrow.now().date(),
			text_body = body
		) 

		price_list_path = os.path.join(".","price_list", str(member.mark_up))
		if not os.path.isdir(price_list_path): raise CannotFindFolder("Cannot find %s folder" % price_list_path)
		for file_path in glob.iglob(os.path.join(price_list_path,"*.xls")):
			envelope.add_attachment(file_path)
		envelope.send(self.mail_server,tls=True)

