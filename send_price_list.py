from lib.price_list_engine.mailer import Mailer
from lib.member.interface  	      import MemberInterface

if __name__ == "__main__":
	members = MemberInterface.get_all(receive_price_list=True)

	for member in members:
		mailer = Mailer()
		mailer.send(member)