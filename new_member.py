from lib.member import Member

def ask_yes_no(message, ok=[], cancel=[]):
	result = input(message)
	result = result.lower()
	ok     = [o.lower() for o in ok]
	cancel = [c.lower() for c in cancel]
	if result in ok:
		return True
	elif result in cancel:
		return False
	return TypeError("Tidak dapat mengenali jawaban.")

if __name__ == "__main__":
	email   = input("Email: ")
	nama    = input("Nama: ")
	mark_up = input("Mark Up: ")
	mark_up = int(mark_up)
	langanan_price_list = ask_yes_no("Langganan Price List [Y/n]: ", ok=["y","ya","yes"], cancel=["n","no"])

	member = Member(email=email, nama=nama, mark_up=mark_up, receive_price_list=langanan_price_list)
	member.save()