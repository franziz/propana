Guide ini dibuat menggunakan Bahasa Indonesia karena software yang dibuat ini dipergunakan hanya untuk kalangan sendiri dan orang Indonesia saja.

Sekilas tentang propanareload.com merupakan sebuah agent pembayaran online yang melayani pembelian pulsa, kuota, maupun token PLN.

#Instalasi

Assumsi yang dipakai dalam instalasi kali ini adalah

- Docker
- Git
- Mongo Container dengan nama "mongo"
- Account Mailgun

1. `docker pull franziz/propana` 
2. `git clone http://github.com/franziz/propana.git`
3. `docker run -it --name propana --link mongo:mongo -v $(PWD)/propana:/root/app franziz/propana`


# Fungsi

`update_price_list.py`

	Mengambil data pricelist dari website http://www.propanareload.com/hargaretail

`generate_price_list.py`

	Melakukan agregasi data dari database kemudian merubah data tersebut menjadi Excel file (*.xls). Hasil dari agregasi dapat dilihat pada folder price_list/. Aggregasi dibedakan menjadi beberapa folder sesuai dengan mark up yang diberika. Contoh: `generate_price_list.py` akan menghasilkan folder price_list/1000/*.xls jika ada member yang memiliki mark up sebesar 1000. Summary: folder pricelist/[Mark UP]/*.xls

`send_price_list.py`

	Mengirim price list ke member-member yang telah terdaftar dan memilih opsi untuk mendapatkan price list.

`send_price_list.sh`

	Mengirimkan pricelist ke semua member yang ada sesuai dengan mark up yang diberikan. Fungsi ini akan memanggil beberapa modul:
	- `update_price_list.py`
	- `generate_price_list.py`
	- `send_price_list.py`
	
`new_member.py`

	Menambahkan member baru kedalam database.

# Migrasi

Migrasi disini berfungsi untuk melakukan migrasi dari server LAMA ke server BARU. Untuk proses instalasi pertama kali, tidak tidak perlu untuk menjalankan script ini. `python3 migration.py`

# Database

Beberapa database yang ada didalam mongo tidak dapat dihapus sama sekali antaralain:
- propana.members