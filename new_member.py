from lib.member            import Member
from lib.exceptions        import InvalidInput, ValidationError
from lib.member.exceptions import DuplicateMember
from curtsies          	   import fmtstr

def ask_yes_no(message, ok=[], cancel=[], default=""):
	result = input(message)
	result = default if not result else result
	result = result.lower()
	ok     = [o.lower() for o in ok]
	cancel = [c.lower() for c in cancel]
	if result in ok:
		return True
	elif result in cancel:
		return False
	return InvalidInput("Tidak dapat mengenali jawaban.")

def ask(message):
	result = input(message)
	if not result: raise InvalidInput("Jawaban tidak boleh kosong.")
	return result

if __name__ == "__main__":
	try:
		email   = ask("Email: ")
		nama    = ask("Nama: ")
		mark_up = ask("Mark Up: ")
		mark_up = int(mark_up)
		langanan_price_list = ask_yes_no("Langganan Price List [Y/n]: ", ok=["y","ya","yes"], cancel=["n","no"], default="y")

		member = Member(email=email, nama=nama, mark_up=mark_up, receive_price_list=langanan_price_list)
		member.save()
		print("[new_member][success] Data member berhasil ditambahkan.")
	except InvalidInput as ex:
		print(fmtstr("[new_member][error] %s" % ex,"red"))
	except DuplicateMember as ex:
		print(fmtstr("[new_member][error] %s" % ex,"red"))
	except ValidationError as ex:
		print(fmtstr("[new_member][error] %s" % ex,"red"))