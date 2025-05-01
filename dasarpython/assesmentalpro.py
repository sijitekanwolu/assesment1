# nama = input("Masukan Nama Lengkap Anda? ")
# nim = input("Masukan NIM Anda? ")
# Lahir = input("Masukan Tanggal Lahir Anda? ")




# nilai_awal = int(input("Input nilai awal: "))
# jumlah_baris = int(input("Jumlah baris: "))

# 10
# for i in range(jumlah_baris):
#     angka = nilai_awal + i
#     if angka % 2 == 0:
#         print(f"{angka} = genap")
#     else:
#         print(f"{angka} = ganjil")


# jumlah_bintang = int(input("Input bintang: "))


# for i in range(jumlah_bintang, 0, -1):
#     print(f"{i} " + "*" * (jumlah_bintang - i + 1))


# var_bil = [104, 136, 25, 78, 2, 19, 7]


# n = len(var_bil)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if var_bil[j] < var_bil[j + 1]:
          
#             var_bil[j], var_bil[j + 1] = var_bil[j + 1], var_bil[j]

# for angka in var_bil:
#     print(angka, end=", ")

# class biodata :
#     def __init__ ( self , nama , nim , umur , gender , alamat ):
#         self . nama = nama
#         self . nim = nim
#         self . umur = umur
#         self . gender = gender
#         self . alamat = alamat

# anggota1 = biodata ("budi", 1, 18, 'L', 'bandung')
# anggota2 = biodata ("wati", 2, 19, 'P', 'jakarta')


# print ( anggota1 . nama , anggota1 . umur )
# print ( anggota2 . nama , anggota2 . umur )


# class biodata:
#     def __init__(self, nama, nim, umur, gender, alamat):
#         self.nama = nama
#         self.nim = nim
#         self.umur = umur
#         self.gender = gender
#         self.alamat = alamat

# anggota1 = biodata("budi", 1, 18, 'L', 'bandung')
# print(anggota1.nama, anggota1.umur)

# anggota1.nama = "amir"
# anggota1.umur = 19

# print(anggota1.nama, anggota1.umur)


class Tanding:
    def __init__(self, petarung1, petarung2):
        self.petarung1 = petarung1
        self.petarung2 = petarung2
        self.pemenang = " "

    def mulai(self):
        """
        Pemenang pertarungan ditentukan dengan cara sbb:
        Setiap sifat antara 2 petarung dibandingkan.
        Yang lebih besar mendapatkan 1 poin.
        Pemenang adalah petarung yang memiliki poin paling besar.
        """
        nilai_petarung1 = 0
        nilai_petarung2 = 0

        # Perbandingan kekuatan
        if self.petarung1.kekuatan > self.petarung2.kekuatan:
            nilai_petarung1 += 1
        elif self.petarung1.kekuatan < self.petarung2.kekuatan:
            nilai_petarung2 += 1

        # Perbandingan kecerdasan
        if self.petarung1.kecerdasan > self.petarung2.kecerdasan:
            nilai_petarung1 += 1
        elif self.petarung1.kecerdasan < self.petarung2.kecerdasan:
            nilai_petarung2 += 1

        # Perbandingan kelincahan
        if self.petarung1.kelincahan > self.petarung2.kelincahan:
            nilai_petarung1 += 1
        elif self.petarung1.kelincahan < self.petarung2.kelincahan:
            nilai_petarung2 += 1

        # Perbandingan senjata
        if self.petarung1.senjata > self.petarung2.senjata:
            nilai_petarung1 += 1
        elif self.petarung1.senjata < self.petarung2.senjata:
            nilai_petarung2 += 1

        # Menentukan pemenang
        if nilai_petarung1 > nilai_petarung2:
            self.pemenang = self.petarung1.nama
        elif nilai_petarung1 < nilai_petarung2:
            self.pemenang = self.petarung2.nama
        else:
            self.pemenang = " "

    def print_pemenang(self):
        if self.pemenang != " ":
            print("Pemenangnya : " + self.pemenang)
        else:
            print("Seri !!")

