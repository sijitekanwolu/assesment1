# def nkarakter(karakter, jumlah):
#     return karakter * jumlah

# # contoh penggunaan
# x = nkarakter("#", 5)

# # perintah ini mencetak ##### ke layar
# print(x)

# def jumlah_karakter(input_string):
   
#     n_karakter = len(input_string)
#     return n_karakter

# # contoh penggunaan
# y = jumlah_karakter("multimedia")

# # perintah ini mencetak angka 10 ke layar
# print(y)


# def maju(posisi):
#     x, y = posisi
#     return (x + 1, y)

# def mundur(posisi):
#     x, y = posisi
#     return (x - 1, y)

# def belok_kanan(posisi):
#     x, y = posisi
#     return (x, y + 1)

# def belok_kiri(posisi):
#     x, y = posisi
#     return (x, y - 1)

# selesai = False
# posisi_robot = (0, 0)  # tuple

# while not selesai:
#     print("-" * 30)
#     print("Pilih perintah untuk robot:")
#     print("1. Maju")
#     print("2. Mundur")
#     print("3. Belok Kanan")
#     print("4. Belok Kiri")
#     print("5. Selesai")
#     print("-" * 30)
    
#     perintah = input("Masukkan perintah: ")
    
#     if not perintah.isdigit():
#         print("Harap masukkan angka yang valid!")
#         continue
    
#     perintah = int(perintah)
    
#     if perintah == 1:
#         posisi_robot = maju(posisi_robot)
#     elif perintah == 2:
#         posisi_robot = mundur(posisi_robot)
#     elif perintah == 3:
#         posisi_robot = belok_kanan(posisi_robot)
#     elif perintah == 4:
#         posisi_robot = belok_kiri(posisi_robot)
#     elif perintah == 5:
#         selesai = True
#     else:
#         print("Perintah tidak valid!")
#         continue
    
#     print(f"Posisi robot sekarang: {posisi_robot}")

# def gerak_robot(posisi, arah):
#     x, y = posisi
#     if arah == "maju":
#         return (x + 1, y)
#     elif arah == "mundur":
#         return (x - 1, y)
#     elif arah == "belok kanan":
#         return (x, y + 1)
#     elif arah == "belok kiri":
#         return (x, y - 1)
#     else:
#         print("Arah tidak valid!")
#         return posisi

# selesai = False
# posisi_robot = (0, 0)  # tuple

# while not selesai:
#     print("-" * 30)
#     print("Pilih perintah untuk robot:")
#     print("1. Maju")
#     print("2. Mundur")
#     print("3. Belok Kanan")
#     print("4. Belok Kiri")
#     print("5. Selesai")
#     print("-" * 30)
    
#     perintah = input("Masukkan perintah: ")
    
#     if not perintah.isdigit():
#         print("Harap masukkan angka yang valid!")
#         continue
    
#     perintah = int(perintah)
    
#     if perintah == 1:
#         posisi_robot = gerak_robot(posisi_robot, "maju")
#     elif perintah == 2:
#         posisi_robot = gerak_robot(posisi_robot, "mundur")
#     elif perintah == 3:
#         posisi_robot = gerak_robot(posisi_robot, "belok kanan")
#     elif perintah == 4:
#         posisi_robot = gerak_robot(posisi_robot, "belok kiri")
#     elif perintah == 5:
#         selesai = True
#     else:
#         print("Perintah tidak valid!")
#         continue
    
#     print(f"Posisi robot sekarang: {posisi_robot}")



# def rekursif():
   
#     print("x")
#     rekursif()

# rekursif()  

# def simpan_data(nama_file):
#     with open(nama_file, "a") as file:
#         while True:
#             nama = input("Masukkan nama (atau ketik 'selesai' untuk berhenti): ")
#             if nama.lower() == "selesai":
#                 break
            
#             nilai = input("Masukkan nilai: ")
#             if not nilai.isdigit():
#                 print("Nilai harus berupa angka!")
#                 continue
            
#             file.write(f"{nama}, {nilai}\n")
#             print("Data berhasil disimpan!")

# nama_file = "data_nilai.txt"
# simpan_data(nama_file)
# print(f"Semua data telah disimpan dalam {nama_file}")


# def tambah(a, b):
#     return a + b

# def kurang(a, b):
#     return a - b

# def kali(a, b):
#     return a * b

# def bagi(a, b):
#     if b == 0:
#         return "Error: Pembagian dengan nol!"
#     return a / b

# def kalkulator():
#     while True:
#         print("\nMenu Kalkulator:")
#         print("(a) Tambah")
#         print("(b) Kurang")
#         print("(c) Kali")
#         print("(d) Bagi")
#         print("(e) Keluar")
#         pilihan = input("Pilih operasi: ").lower()
        
#         if pilihan == 'e':
#             print("Keluar dari program.")
#             break
        
#         if pilihan not in ['a', 'b', 'c', 'd']:
#             print("Pilihan tidak valid! Coba lagi.")
#             continue
        
#         try:
#             num1 = float(input("Masukkan angka pertama: "))
#             num2 = float(input("Masukkan angka kedua: "))
#         except ValueError:
#             print("Harap masukkan angka yang valid!")
#             continue
        
#         if pilihan == 'a':
#             print(f"Hasil: {tambah(num1, num2)}")
#         elif pilihan == 'b':
#             print(f"Hasil: {kurang(num1, num2)}")
#         elif pilihan == 'c':
#             print(f"Hasil: {kali(num1, num2)}")
#         elif pilihan == 'd':
#             print(f"Hasil: {bagi(num1, num2)}")

# kalkulator()

# import random

# def baca_kata_dari_file(nama_file):
#     with open(nama_file, "r") as file:
#         return [line.strip() for line in file.readlines()]

# def tampilkan_kata(kata, tebakan):
#     return " ".join([huruf if huruf in tebakan else "_" for huruf in kata])

# def tebak_kata():
#     nama_file = "daftar_kata.txt"
#     daftar_kata = baca_kata_dari_file(nama_file)
#     kata_rahasia = random.choice(daftar_kata)
#     tebakan = set()
#     percobaan = 10
    
#     print("Selamat datang di permainan Tebak Kata!")
#     while percobaan > 0:
#         print(f"\nKata: {tampilkan_kata(kata_rahasia, tebakan)}")
#         print(f"Sisa percobaan: {percobaan}")
#         huruf = input("Tebak satu huruf: ").lower()
        
#         if len(huruf) != 1 or not huruf.isalpha():
#             print("Masukkan satu huruf yang valid!")
#             continue
        
#         if huruf in tebakan:
#             print("Anda sudah menebak huruf ini.")
#             percobaan -= 1  # Mengurangi percobaan jika pengguna mengulang tebakan
#             continue
        
#         tebakan.add(huruf)
#         percobaan -= 1  # Mengurangi percobaan setiap kali menebak
        
#         if huruf not in kata_rahasia:
#             print("Huruf tidak ada dalam kata.")
        
#         if all(h in tebakan for h in kata_rahasia):
#             print(f"Selamat! Anda berhasil menebak kata: {kata_rahasia}")
#             return
    
#     print(f"Maaf, Anda kehabisan percobaan. Kata yang benar adalah: {kata_rahasia}")

# # Pastikan file daftar_kata.txt sudah ada dengan 20 kata di dalamnya
# tebak_kata()