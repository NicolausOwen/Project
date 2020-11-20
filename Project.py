from os import system

def menu():
	system("cls")
	print("""
Program Perpustakaan
[1]. Daftar Buku
[2]. Tambah Buku Baru
[3]. Cari Buku
[4]. Hapus buku
[Q]. Keluar
		""")

def kosong(kontainer):
	if len(kontainer) != 0:
		return True
	else:
		return False

def Cek_jawaban(user):
	if user.upper() == "Y":
		return True
	else:
		return False

def print_data(Buku=None, Judul=True, Isbn=True, all_data=False):
	if Buku != None and all_data == False:
		print(f"NAMA : {Buku}")
		print(f"Judul Buku : {Daftar[Buku]['Judul']}")
		print(f"Isbn : {Daftar[Buku]['Isbn']}")
	elif Isbn == False and all_data == False:
		print(f"NAMA : {Buku}")
		print(f"Judul buku : {Daftar[Buku]['Judul']}")
	elif all_data == True:
		for every_Buku in Daftar: # lists, string, dict
			nama = every_Buku # nama = key dari dict-nya
			Judul = Daftar[every_Buku]["Judul"]
			Isbn = Daftar[every_Buku]["Isbn"]
			print(f"\nNama Penulis: {nama} \nJudul Buku : {Judul} \nNo ISBN : {Isbn}")


def Daftar_buku():
	system("cls")
	print("BUKU YANG TERSEDIA")
	if kosong(Daftar):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA BUKU YANG TERSIMPAN")
	input("Tekan ENTER untuk kembali")

def tambah_Buku():
	system("cls")
	print("Menambahkan Buku Baru")
	nama = input("Nama Penulis : ")
	Judul = input("Judul buku : ")
	Isbn = input("ISBN : ")
	respon = input(f"Apakah yakin ingin Karya : {nama} ? (Y/N) ")
	if Cek_jawaban(respon):
		Daftar[nama] = {
			"Judul" : Judul,
			"Isbn" : Isbn
		}
		print("Buku Tersimpan.")
	else:
		print("Batal Disimpan")
	input("Tekan ENTER untuk kembali")

def searching(Buku):
	if Buku in Daftar:
		return True
	else:
		return False

def cari_Buku():
	system("cls")
	print("MENCARI BUKU")
	nama = input("Nama penulis yang Dicari : ")
	exists = searching(nama)
	if exists:
		system("cls")
		print_data(Buku=nama)
	else:
		print("Karya Buku Tidak Ada")
	input("Tekan ENTER untuk kembali")

def Hapus_Buku():
	system("cls")
	print("PENGHAPUS BUKU")
	nama = input("Nama penulis Karya yang akan Dihapus : ")
	exists = searching(nama)
	if exists:
		print_data(Buku=nama)
		respon = input(f"Yakin ingin menghapus Karya {nama} ? (Y/N) ")
		if Cek_jawaban(respon):
			del Daftar[nama]
			print("Buku Telah Dihapus")
		else:
			print("Buku Batal Dihapus")
	else:
		print("Karya Penulis Tidak Ada")
	input("Tekan ENTER untuk kembali")

def check_user(user):
	user = user.upper()
	if user == "Q":
		print("Good bye")
		return True
	elif user == "1":
		Daftar_buku()
	elif user == "2":
		tambah_Buku()
	elif user == "3":
		cari_Buku()
	elif user == "4":
		Hapus_Buku()

Daftar = {
	"Muray Enkin" : {
		"Judul" : "A Guide To A EffectiveCare In Pregnancy And Child Birth",
		"Isbn" : "019 262326 5"

	},
	"Tarwoto" : {
		"Judul" : "Anemia Pada Ibu Hamil",
		"Isbn" : "978 979 15135 3 1 7"
	}
}

stop = False
while not stop:
	menu()
	user = input("Pilihan : ")
	stop = check_user(user)

