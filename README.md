Guide ini dibuat menggunakan Bahasa Indonesia karena software yang dibuat ini dipergunakan hanya untuk kalangan sendiri dan orang Indonesia saja.

Sekilas tentang propanareload.com merupakan sebuah agent pembayaran online yang melayani pembelian pulsa, kuota, maupun token PLN.

#Instalasi
Assumsi yang dipakai dalam instalasi kali ini adalah
- Docker
- Git
- Mongo Container dengan nama "mongo"

1. `docker pull franziz/propana` 
2. `git clone http://github.com/franziz/propana.git`
3. `docker run -it --name propana --link mongo:mongo -v $(PWD)/propana:/root/app franziz/propana`

Pastikan cron dan postfix telah dinyalakan dengan cara memanggil perintah `ps ax`

# Fungsi
send_price_list.sh
	Mengirimkan pricelist ke semua member yang ada sesuai dengan mark up yang diberikan. Fungsi ini akan memanggil beberapa modul:
	- update_price_list.py
	- generate_price_list.py
	- send_price_list.py
new_member.py
	Menambahkan member baru kedalam database.