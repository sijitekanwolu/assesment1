import random
import json


class Petarung:
    def __init__(self, nama, kekuatan, kecerdasan, kelincahan, senjata, 
                 kesehatan=100, menang=0, kalah=0, seri=0):
        self.nama = nama
        self.kekuatan = kekuatan
        self.kecerdasan = kecerdasan
        self.kelincahan = kelincahan
        self.senjata = senjata
        self.kesehatan = kesehatan
        self.menang = menang
        self.kalah = kalah
        self.seri = seri

    def tampil(self):
        print(f"Nama: {self.nama}")
        print(f"Kekuatan: {self.kekuatan}")
        print(f"Kecerdasan: {self.kecerdasan}")
        print(f"Kelincahan: {self.kelincahan}")
        print(f"Senjata: {self.senjata}")
        print(f"Kesehatan: {self.kesehatan}")
        print(f"Menang: {self.menang} | Kalah: {self.kalah} | Seri: {self.seri}")

    def simpan(self):
        with open(f"petarung/{self.nama}.json", "w") as file:
            json.dump(self.__dict__, file)

    @staticmethod
    def load(nama):
        with open(f"petarung/{nama}.json") as file:
            data = json.load(file)
            return Petarung(**data)

    def reset_status(self):
        if self.kesehatan >= 10:
            self.kesehatan -= 10
            self.kekuatan = random.randint(1, 10)
            self.kecerdasan = random.randint(1, 10)
            self.kelincahan = random.randint(1, 10)
            self.senjata = random.randint(1, 10)
            print(f"{self.nama} telah direset. Kesehatan -10.")
        else:
            print("Kesehatan tidak cukup untuk reset.")
