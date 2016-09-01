""" Script ini berrfungsi untuk melakukan migrasi terhadap server baru.
	Biasanya terdapat perbedaan dalam struktur database  yang tidak dapat berubah. 
	Adapun struktu database yang tidak dapat berubah dapat dilihat pada bagian README.md

	Dikarena sifatnya yang tidak boleh dihapus, maka untuk melakukan migrasi ke server baru, 
	di wajibkan untuk menggunakan script dibawah ini
""" 
from lib.member   import Member
from lib.database import Database

if __name__ == "__main__":
	db = Database.get_db()

	# Field yang wajib ada dalam propana.members
	member = Member()
	fields = vars(member)

	for member in db.members.find():
		for field, value in fields.items():
			if field not in member: 
				print("[migration][debug] Injeksi field %s ke member %s" % (field, member["nama"]))
				db.members.update({"_id":member["_id"]},{"$set":{field:value}})