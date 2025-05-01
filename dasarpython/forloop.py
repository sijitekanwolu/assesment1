# material = ["air", "api", "udara", "tanah"]

# for x in material:
#    if x == "udara":
#     break
   
#    print(x)

#  ////////////////////////////////////////////////

# person = {'nama' : 'sule', 'umur' : 30, 'alamat' : 'bojong santos'}

# print(person['nama'], person['umur'], person['alamat']) 

# print("Interasi melalui kunci")
# for key in person:
#   print(key)

# /////////////////////////////////////////////////

# kotak = int(input("masukan jumlah pixel kotak: "))
# for y in range(kotak):
#      px=""
#      for x in range(kotak):
#           px = "*"+px
#      print(px)

# import os

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def main_menu():
#     while True:
#         clear_screen()
#         print("############################")
#         print("1. Pilihan 1")
#         print("2. Pilihan 2")
#         print("3. Pilihan 3")
#         print("4. Keluar")
#         print("############################")
        
#         pilihan = input("Masukkan pilihan Anda: ")
        
#         if pilihan == '1':
#             print("Anda memilih angka 1. Tekan Enter untuk melanjutkan")
#             input()
#         elif pilihan == '2':
#             print("Anda memilih angka 2. Tekan Enter untuk melanjutkan")
#             input()
#         elif pilihan == '3':
#             print("Anda memilih angka 3. Tekan Enter untuk melanjutkan")
#             input()
#         elif pilihan == '4':
#             print("Terima kasih")
#             break
#         else:
#             print("Anda tidak memilih dengan benar")
#             input("Tekan Enter untuk kembali ke menu...")

# if __name__ == "__main__":
#     main_menu()   


# daftar_nama = {}

# # Meminta input 10 nama dari pengguna
# for i in range(10):
#     nama = input("Masukkan nama ke-" + str(i + 1) + ": ")
#     huruf_awal = nama[0].upper()  # Gunakan huruf kapital agar konsisten
    
#     if huruf_awal in daftar_nama:
#         daftar_nama[huruf_awal].append(nama)  # Jika sudah ada, tambahkan ke daftar
#     else:
#         daftar_nama[huruf_awal] = [nama]  # Jika belum ada, buat daftar baru

# # Menampilkan hasil dengan rapi
# print("\nDaftar Nama Berdasarkan Huruf Awal:")
# for huruf, nama_list in sorted(daftar_nama.items()):
#     print(f"{huruf}: {', '.join(nama_list)}") 


# for i in range(5, 0, -1):
#     print('*' * i)

# for i in range(2, 6):
#     print('$' * i)

# import random

# # Generate angka acak antara 1-100
# angka_rahasia = random.randint(1, 100)

# print("Tebak angka antara 1-100!")
# while True:
#     try:
#         tebakan = int(input("Masukkan tebakanmu: "))
#         if tebakan < angka_rahasia:
#             print("Terlalu kecil!")
#         elif tebakan > angka_rahasia:
#             print("Terlalu besar!")
#         else:
#             print("Tepat!")
#             break
#     except ValueError:
#         print("Masukkan angka yang valid!")

