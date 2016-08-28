from lib.price_list_engine.generator import Generator
from lib.member.interface            import MemberInterface
import shutil

if __name__ == "__main__":
	members  = MemberInterface.get_all()	
	mark_ups = [member.mark_up for member in members]
	mark_ups = list(set(mark_ups))

	Generator.clean_directory()
	for mark_up in mark_ups:		
		Generator.generate("PULSA", mark_up)
		Generator.generate("KUOTA", mark_up)
		Generator.generate("TOKEN", mark_up)
		Generator.generate("PAKET", mark_up)