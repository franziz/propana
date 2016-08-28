from lib.member import Member

if __name__ == "__main__":
	email = input("Email: ")
	nama  = input("Nama: ")
	mark_up = input("Mark Up: ")
	mark_up = int(mark_up)

	member = Member(email=email, nama=nama, mark_up=mark_up)
	member.save()