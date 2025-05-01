from datetime import datetime, timedelta


class Sewa:
    BIAYA_PER_JAM = 50000  # Tarif sewa per jam

    def __init__(self, nama_penyewa, no_telp, tanggal_sewa, jam_mulai, jam_selesai):
        self.nama_penyewa = nama_penyewa
        self.no_telp = no_telp
        self.tanggal_sewa = tanggal_sewa
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai

    def hitung_durasi(self):
        fmt = "%H:%M" 
        jam_mulai_benar = self.jam_mulai.replace('.', ':') 
        jam_selesai_benar = self.jam_selesai.replace('.', ':') 

        mulai = datetime.strptime(jam_mulai_benar, fmt)
        selesai = datetime.strptime(jam_selesai_benar, fmt)
       

        if selesai < mulai:
            selesai += timedelta(days=1)

        durasi = (selesai - mulai).seconds / 3600
        return durasi

    def hitung_biaya(self):
        durasi = self.hitung_durasi()
        return durasi * self.BIAYA_PER_JAM
     

    def to_list(self):
        return [
            self.nama_penyewa,
            self.no_telp,
            self.tanggal_sewa,
            self.jam_mulai,
            self.jam_selesai
        ]

    @staticmethod
    def from_list(data_list):
        return Sewa(*data_list)
