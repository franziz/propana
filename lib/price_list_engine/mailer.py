from ..member     import Member
from ..exceptions import CannotFindFolder
from ..mailgun    import Mailgun
from curtsies     import fmtstr
import os
import arrow
import glob

class Mailer:
	def __init__(self):
		pass

	def send(self, member=None):
		try:
			assert member       is not None, "member is not defined."
			assert type(member) is Member  , "incorrect member data type."
			assert member.nama  is not None, "nama is not defined."
			assert member.email is not None, "email is not defined."

			template_path = os.path.join(".","templates")
			if not os.path.isdir(template_path): raise CannotFindFolder("Cannot find %s folder" % template_path)
			body = open(os.path.join(template_path, "price_list.smet"),"r")
			body = body.read()
			body = body.format(tanggal=arrow.now().date(), nama=member.nama)

			msg = Mailgun()
			msg.set_sender("Syuping Mobile", "pricelist@syuping.com")
			msg.add_recipient(member.nama, member.email)

			price_list_path = os.path.join(".","price_list", str(member.mark_up))
			if not os.path.isdir(price_list_path): raise CannotFindFolder("Cannot find %s folder" % price_list_path)
			for file_path in glob.iglob(os.path.join(price_list_path,"*.xls")):
				msg.add_attachment(file_path)

			msg.send(text=body, subject="Price List %s" % arrow.now().date())
		except requests.exceptions.ConnectionError as ex:
			print(fmtstr("[mailer][error] %s" % ex, "red"))

