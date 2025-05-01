import random

class Tanding:
    def __init__(self, petarung1, petarung2):
        self.petarung1 = petarung1
        self.petarung2 = petarung2
        self.pemenang = " "

    def mulai(self):
        nilai1 = 0
        nilai2 = 0

        atribut = ['kekuatan', 'kecerdasan', 'kelincahan', 'senjata']
        for attr in atribut:
            if getattr(self.petarung1, attr) > getattr(self.petarung2, attr):
                nilai1 += 1
            elif getattr(self.petarung1, attr) < getattr(self.petarung2, attr):
                nilai2 += 1

        if nilai1 > nilai2:
            self.pemenang = self.petarung1.nama
            self.petarung1.menang += 1
            self.petarung2.kalah += 1
            self.petarung2.kesehatan -= 5
            self.petarung1.kekuatan += random.randint(1, 5)
        elif nilai1 < nilai2:
            self.pemenang = self.petarung2.nama
            self.petarung2.menang += 1
            self.petarung1.kalah += 1
            self.petarung1.kesehatan -= 5
            self.petarung2.kekuatan += random.randint(1, 5)
        else:
            self.pemenang = " "
            self.petarung1.seri += 1
            self.petarung2.seri += 1

    def print_pemenang(self):
        if self.pemenang != " ":
            print("Pemenangnya: " + self.pemenang)
        else:
            print("Seri!!")
