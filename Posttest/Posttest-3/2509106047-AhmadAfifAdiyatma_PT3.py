import random
from abc import ABC, abstractmethod


class Film:
    def __init__(self, judul, genre, durasi):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi


# Komposisi
class KodeBooking:
    def __init__(self, nomor):
        self.kode = "CGV-" + str(nomor)


# Asosiasi + Duck Typing (kelas 1)
class MesinCetak:
    def __init__(self, nama_mesin):
        self.nama_mesin = nama_mesin

    def kirim(self, pesan):
        print(f"[{self.nama_mesin}] mencetak -> {pesan}")


# Duck Typing (kelas 2, tidak ada hubungan pewarisan dengan MesinCetak)
class NotifikasiEmail:
    def __init__(self, alamat_email):
        self.alamat_email = alamat_email

    def kirim(self, pesan):
        print(f"[Email ke {self.alamat_email}] -> {pesan}")


# Duck Typing
def kirim_notifikasi(media, pesan):
    media.kirim(pesan)


# Abstraksi (Abstract Class) + OCP
class Tiket(ABC):
    nama_bioskop = "CGV"
    pajak = 0.11

    def __init__(self, film, kursi, harga):
        self.film = film                 # Agregasi: Film dibuat di luar, dikirim ke sini
        self.kursi = kursi
        self._harga = harga              # protected, perlu diakses subclass
        self.__kode = KodeBooking(random.randint(1000, 9999))  # Komposisi, private

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Harga tidak boleh 0 atau minus")
        self._harga = harga_baru

    @abstractmethod
    def hitung_biaya_tambahan(self):
        pass

    @abstractmethod
    def deskripsi_fasilitas(self):
        pass

    def total_harga(self):
        subtotal = self._harga + (self._harga * Tiket.pajak)
        return subtotal + self.hitung_biaya_tambahan()

    def info_tiket(self):
        print(f"{self.film.judul} - Kursi {self.kursi}")
        print(self.deskripsi_fasilitas())
        print(f"Total: Rp{self.total_harga():,.0f}")
        print("Kode Booking:", self.__kode.kode)

    # Operator Overloading
    def __str__(self):
        return f"{self.film.judul} | Kursi {self.kursi} | Rp{self.total_harga():,.0f}"

    def __add__(self, tiket_lain):
        if not isinstance(tiket_lain, Tiket):
            return NotImplemented
        return self.total_harga() + tiket_lain.total_harga()


# Inheritance + Polimorfisme (subclass 1)
class TiketReguler(Tiket):
    def __init__(self, film, kursi, harga, bonus_air_mineral=True):
        super().__init__(film, kursi, harga)
        self.bonus_air_mineral = bonus_air_mineral

    def hitung_biaya_tambahan(self):
        return 0

    def deskripsi_fasilitas(self):
        if self.bonus_air_mineral:
            return "Reguler + bonus air mineral gratis"
        return "Reguler"


# Inheritance + Polimorfisme (subclass 2)
class TiketVip(Tiket):
    biaya_vip = 25000

    def __init__(self, film, kursi, harga, nomor_sofa):
        super().__init__(film, kursi, harga)
        self.nomor_sofa = nomor_sofa

    def hitung_biaya_tambahan(self):
        return TiketVip.biaya_vip

    def deskripsi_fasilitas(self):
        return f"VIP sofa {self.nomor_sofa}, reclining seat"

    def __str__(self):
        return super().__str__() + f" [Sofa {self.nomor_sofa}]"


# OCP (subclass baru, ditambah tanpa mengubah Tiket, Transaksi, atau subclass lain)
class TiketPelajar(Tiket):
    biaya_admin = 2000

    def __init__(self, film, kursi, harga, nomor_kartu_pelajar):
        super().__init__(film, kursi, harga)
        self.nomor_kartu_pelajar = nomor_kartu_pelajar

    def hitung_biaya_tambahan(self):
        return TiketPelajar.biaya_admin

    def deskripsi_fasilitas(self):
        return f"Pelajar, kartu {self.nomor_kartu_pelajar}"


# Agregasi
class Transaksi:
    diskon_member = 0.1

    def __init__(self, member=False):
        self.member = member
        self.__daftar_tiket = []

    def tambah(self, tiket):
        if not isinstance(tiket, Tiket):
            raise TypeError("Yang ditambahkan harus objek Tiket")
        self.__daftar_tiket.append(tiket)

    def __len__(self):
        return len(self.__daftar_tiket)

    def bayar(self):
        total = sum(t.total_harga() for t in self.__daftar_tiket)
        if self.member:
            total -= total * Transaksi.diskon_member
        return total

    # Polimorfisme (loop berisi objek dari subclass berbeda, perilakunya beda-beda sendiri)
    def struk(self):
        if len(self.__daftar_tiket) == 0:
            print("Belum ada tiket di transaksi ini.")
            return
        print("STRUK PEMBAYARAN")
        for t in self.__daftar_tiket:
            print("-", t)
            print("  ", t.deskripsi_fasilitas())
        status = "Member" if self.member else "Umum"
        print("Status:", status)
        print(f"Total Bayar: Rp{self.bayar():,.0f}")

    # Asosiasi (MesinCetak diterima lewat parameter, dipakai sesaat, tidak disimpan sebagai atribut)
    def cetak_struk_fisik(self, mesin):
        isi = f"Struk a.n. {'Member' if self.member else 'Umum'}, total Rp{self.bayar():,.0f}"
        mesin.kirim(isi)


# MAIN PROGRAM
print("=== DAFTAR FILM ===")
film1 = Film("Avengers: Doomsday", "Action", 150)
film2 = Film("Spider-Man: Brand New Day", "Action", 130)
print(film1.judul, "-", film1.genre, "-", film1.durasi, "menit")
print(film2.judul, "-", film2.genre, "-", film2.durasi, "menit")

print("\n=== PEMBUATAN TIKET (POLIMORFISME VIA PEWARISAN) ===")
tiket1 = TiketReguler(film1, "A1", 50000)
tiket2 = TiketVip(film1, "B5", 85000, nomor_sofa="S1")
tiket3 = TiketPelajar(film2, "C3", 35000, nomor_kartu_pelajar="2409106050")

daftar_tiket_demo = [tiket1, tiket2, tiket3]
for t in daftar_tiket_demo:
    t.info_tiket()
    print()

print("=== BUKTI ABSTRACT CLASS TIDAK BISA DIINSTANSIASI ===")
try:
    t_gagal = Tiket(film1, "X1", 50000)
except TypeError as e:
    print("Gagal membuat objek Tiket langsung:")
    print(e)

print("\n=== SETTER HARGA (VALIDASI) ===")
tiket1.harga = 60000
print("Harga tiket1 setelah diubah:", tiket1.harga)
try:
    tiket1.harga = -5000
except ValueError as e:
    print("Gagal mengubah harga:", e)

print("\n=== OPERATOR OVERLOADING ===")
print("str(tiket2) ->", tiket2)
print("tiket1 + tiket2 ->", tiket1 + tiket2)

print("\n=== TRANSAKSI (AGREGASI) ===")
transaksi1 = Transaksi(member=True)
transaksi2 = Transaksi(member=False)

transaksi1.tambah(tiket1)
transaksi1.tambah(tiket2)
transaksi1.struk()
print("Jumlah tiket di transaksi1 (pakai __len__):", len(transaksi1))

print()
transaksi2.tambah(tiket3)
transaksi2.struk()

print("\n=== ASOSIASI: TRANSAKSI MENGGUNAKAN MESINCETAK ===")
mesin_kasir = MesinCetak("Printer Kasir 1")
transaksi1.cetak_struk_fisik(mesin_kasir)

print("\n=== DUCK TYPING ===")
email_pelanggan = NotifikasiEmail("pelanggan@email.com")
pesan = "Tiket Anda sudah siap diambil"
kirim_notifikasi(mesin_kasir, pesan)
kirim_notifikasi(email_pelanggan, pesan)