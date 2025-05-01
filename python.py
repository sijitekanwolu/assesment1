

# a=19
# b=10

# if (a<b):
#     print("pinter")
# else:
#     print("gwendeng")

#////////////////////////////////////////////////////////////////////////////////

# Daftar kata yang akan diurutkan
# words = ["jeruk", "apel", "mangga", "pisang", "anggur"]

# Mengurutkan daftar sesuai abjad
# sorted_nama = sorted(nama)

# print("Daftar setelah diurutkan:", sorted_nama)

# TUGAS ALPRO

# 1.
# from collections import defaultdict

# def group_names():
#     name_dict = defaultdict(list)  # Dictionary dengan nilai default berupa list
    
#     print("Masukkan 10 nama:")
#     for _ in range(10):
#         name = input("Nama: ").strip()
        # if name:  # Pastikan input tidak kosong
            # initial = name[0].upper()  # Ambil huruf awal dan ubah jadi huruf besar
#             name_dict[initial].append(name)
    
#     return dict(name_dict)

# if __name__ == "__main__":
#     grouped_names = group_names()
#     print("\nHasil Pengelompokan Nama:")
#     for key, names in grouped_names.items():
#         print(f"{key}: {names}")


# 2.
# import random

# def tebak_angka():
#     angka_rahasia = random.randint(1, 100)  # Angka acak antara 1-100
#     tebakan = int(input("Tebak angka (1-100): "))
    
#     selisih = abs(angka_rahasia - tebakan)
    
#     if selisih < 10:
#         print("Menang!")
#     elif 10 <= selisih <= 30:
#         print("Hampir!")
#     else:
#         print("Jauh!")
    
#     print(f"Angka yang benar: {angka_rahasia}")

# tebak_angka()


 # 3.
# barang = {
#     1: ("Laptop", 7500000),
#     2: ("Smartphone", 5000000),
#     3: ("Headphone", 750000),
#     4: ("Keyboard", 350000),
#     5: ("Mouse", 200000),
#     6: ("Monitor", 1500000),
#     7: ("Printer", 1200000),
#     8: ("Flashdisk", 100000),
#     9: ("Hard Drive", 900000),
#     10: ("Webcam", 600000)
# }

# # Menampilkan daftar barang
# print("Daftar Barang:")
# for key, value in barang.items():
#     print(f"{key}. {value[0]} - Rp {value[1]:,}")

# # Meminta input dari user
# try:
#     pilihan = int(input("Masukkan nomor barang yang ingin Anda beli: "))
    
#     if pilihan in barang:
#         nama_barang, harga = barang[pilihan]
#         print(f"Anda memilih {nama_barang} dengan harga Rp {harga:,}")
#     else:
#         print("Maaf, nomor barang tidak tersedia.")
# except ValueError:
#     print("Input tidak valid! Masukkan angka yang sesuai.")


# 4.
# # Meminta pengguna memasukkan dua angka
# angka1 = float(input("Masukkan angka pertama: "))
# angka2 = float(input("Masukkan angka kedua: "))

# # Memilih operasi
# operator = input("Masukkan operator (+, -, *, /): ")

# # Melakukan perhitungan sesuai operator
# if operator == "+":
#     hasil = angka1 + angka2
# elif operator == "-":
#     hasil = angka1 - angka2
# elif operator == "*":
#     hasil = angka1 * angka2
# elif operator == "/":
#     if angka2 != 0:
#         hasil = angka1 / angka2
#     else:
#         hasil = "Error! Tidak bisa dibagi dengan nol."
# else:
#     hasil = "Operator tidak valid!"

# # Menampilkan hasil
# print("Hasil:", hasil)



# 5.
# # Daftar angka yang akan diurutkan
# angka = input("Masukan angka (gunakan spasi): ")
# sorted_angka = list(map(int, angka.split()))

# #  Mengurutkan daftar sesuai abjad
# sorted_angka.sort()

# print("Daftar setelah diurutkan:", sorted_angka)


# 6.
# list_nama = ["ucup", "bani", "nopal", "uki", "parel", "rizal"]

# nama = input ("Masukan Nama Anda: ")

# if nama in list_nama:
#     print("Nama Anda Terdaftar")
# else:
#     print("Nama Anda Tidak Terdaftar")


# 7.
# # Daftar menu makanan dan minuman
# menu_makanan = {
#     "1": {"nama": "Nasi Goreng", "harga": 15000},
#     "2": {"nama": "Mie Ayam", "harga": 12000},
#     "3": {"nama": "Ayam Geprek", "harga": 18000},
# }

# menu_minuman = {
#     "1": {"nama": "Es Teh Manis", "harga": 5000},
#     "2": {"nama": "Jus Alpukat", "harga": 10000},
#     "3": {"nama": "Kopi Susu", "harga": 8000},
# }

# # Menampilkan menu makanan
# print("=== Menu Makanan ===")
# for key, item in menu_makanan.items():
#     print(f"{key}. {item['nama']} - Rp{item['harga']}")

# # Memilih makanan
# pilihan_makanan = input("Pilih makanan (1/2/3): ")
# if pilihan_makanan in menu_makanan:
#     makanan_terpilih = menu_makanan[pilihan_makanan]
# else:
#     print("Pilihan tidak valid! Silakan mulai ulang.")
#     exit()

# # Menampilkan menu minuman
# print("\n=== Menu Minuman ===")
# for key, item in menu_minuman.items():
#     print(f"{key}. {item['nama']} - Rp{item['harga']}")

# # Memilih minuman
# pilihan_minuman = input("Pilih minuman (1/2/3): ")
# if pilihan_minuman in menu_minuman:
#     minuman_terpilih = menu_minuman[pilihan_minuman]
# else:
#     print("Pilihan tidak valid! Silakan mulai ulang.")
#     exit()

# # Menghitung total harga
# total_harga = makanan_terpilih["harga"] + minuman_terpilih["harga"]

# # Menampilkan pesanan dan total harga
# print("\n=== Pesanan Anda ===")
# print(f"Makanan: {makanan_terpilih['nama']} - Rp{makanan_terpilih['harga']}")
# print(f"Minuman: {minuman_terpilih['nama']} - Rp{minuman_terpilih['harga']}")
# print(f"Total yang harus dibayar: Rp{total_harga}")



