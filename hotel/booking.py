import time

# Data kamar hotel (kamarnya tetap untuk contoh sederhana)
rooms = {
    101: {"tipe": "Single", "harga": 300000, "status": "Tersedia"},
    102: {"tipe": "Double", "harga": 500000, "status": "Tersedia"},
    103: {"tipe": "Suite", "harga": 800000, "status": "Tersedia"},
}

# Data pemesanan
bookings = {}

def tampilkan_kamar():
    print("\nDaftar Kamar Hotel:")
    for nomor, info in rooms.items():
        print(f" - Kamar {nomor} | {info['tipe']} | Rp {info['harga']} | Status: {info['status']}")

def pesan_kamar():
    tampilkan_kamar()
    nama = input("\nNama pelanggan: ")
    try:
        nomor_kamar = int(input("Masukkan nomor kamar yang ingin dipesan: "))
        if nomor_kamar in rooms and rooms[nomor_kamar]["status"] == "Tersedia":
            rooms[nomor_kamar]["status"] = "Dipesan"
            bookings[nama] = {
                "kamar": nomor_kamar,
                "status": "Belum Check-in"
            }
            print(f"\n✅ Kamar {nomor_kamar} berhasil dipesan atas nama {nama}.")
        else:
            print("❌ Kamar tidak tersedia atau nomor tidak valid.")
    except ValueError:
        print("❌ Masukkan nomor kamar yang valid.")

def check_in():
    nama = input("\nNama pelanggan untuk check-in: ")
    if nama in bookings:
        nomor_kamar = bookings[nama]["kamar"]
        if bookings[nama]["status"] == "Belum Check-in":
            bookings[nama]["status"] = "Sudah Check-in"
            rooms[nomor_kamar]["status"] = "Terisi"
            print(f"✅ {nama} berhasil check-in di kamar {nomor_kamar}.")
        else:
            print("ℹ️ Anda sudah check-in sebelumnya.")
    else:
        print("❌ Data pemesanan tidak ditemukan.")

def lihat_status():
    if not bookings:
        print("\nBelum ada pemesanan.")
        return
    print("\nStatus Pemesanan:")
    for nama, info in bookings.items():
        print(f" - {nama} | Kamar {info['kamar']} | Status: {info['status']}")

def menu():
    while True:
        print("\n=== APLIKASI PESAN & CHECK-IN HOTEL ===")
        print("1. Lihat Daftar Kamar")
        print("2. Pesan Kamar")
        print("3. Check-in")
        print("4. Lihat Status Pemesanan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_kamar()
        elif pilihan == "2":
            pesan_kamar()
        elif pilihan == "3":
            check_in()
        elif pilihan == "4":
            lihat_status()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi hotel!")
            break
        else:
            print("❌ Pilihan tidak valid.")

# Jalankan program
menu()
