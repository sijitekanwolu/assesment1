from petarung import Petarung
from tanding import Tanding
import os
import random

if not os.path.exists("petarung"):
    os.mkdir("petarung")

def menu():
    while True:
        print("\nMenu:")
        print("(a) Lihat Petarung")
        print("(b) Edit Petarung")
        print("(c) Tambah Petarung")
        print("(d) Hapus Petarung")
        print("(e) Bertanding")
        print("(f) Keluar")
        pilih = input("Pilih menu: ").lower()

        if pilih == "a":
            for file in os.listdir("petarung"):
                petarung = Petarung.load(file[:-5])
                petarung.tampil()
                print("-" * 30)
        elif pilih == "b":
            nama = input("Nama petarung: ")
            if os.path.exists(f"petarung/{nama}.json"):
                p = Petarung.load(nama)
                p.reset_status()
                p.simpan()
        elif pilih == "c":
            nama = input("Nama: ")
            p = Petarung(
                nama,
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10)
            )
            p.simpan()
            print("Petarung ditambahkan!")
        elif pilih == "d":
            nama = input("Nama petarung: ")
            try:
                os.remove(f"petarung/{nama}.json")
                print("Petarung dihapus.")
            except FileNotFoundError:
                print("Petarung tidak ditemukan.")
        elif pilih == "e":
            nama1 = input("Nama petarung 1: ")
            nama2 = input("Nama petarung 2: ")
            if os.path.exists(f"petarung/{nama1}.json") and os.path.exists(f"petarung/{nama2}.json"):
                p1 = Petarung.load(nama1)
                p2 = Petarung.load(nama2)
                t = Tanding(p1, p2)
                t.mulai()
                t.print_pemenang()
                p1.simpan(), p2.simpan()
            else:
                print("Salah satu petarung tidak ditemukan.")
        elif pilih == "f":
            print("Keluar program.")
            break
        else:
            print("Menu tidak valid.")

menu()
