import random

class Film:
    def __init__(self, judul, genre, durasi):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi

    def tampilkan(self):
        print(self.judul, "-", self.genre, "-", self.durasi, "menit")


class KodeBooking:
    def __init__(self, nomor):
        self.kode = "CGV-" + str(nomor)

    def tampilkan(self):
        print("Kode Booking:", self.kode)


class MesinCetak:
    def __init__(self, nama_mesin):
        self.nama_mesin = nama_mesin

    def cetak(self, teks):
        print(f"[{self.nama_mesin}] mencetak -> {teks}")

class Tiket:
    nama_bioskop = "CGV"
    pajak = 0.11

    def __init__(self, film, kursi, harga):
        self.film = film 
        self.kursi = kursi
        self._harga = harga 
        self.__kode = KodeBooking(random.randint(1000, 9999))

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            print("Harga gak boleh 0 atau minus")
        else:
            self._harga = harga_baru

    def total_harga(self):
        return self._harga + (self._harga * Tiket.pajak)

    def cetak(self):
        print(self.film.judul, "- Kursi", self.kursi)
        print("Harga:", self._harga, "| Total dengan pajak:", self.total_harga())
        self.__kode.tampilkan()

    @staticmethod
    def cek_jenis(jenis):
        jenis_tersedia = ["reguler", "3d", "vip"]
        return jenis.lower() in jenis_tersedia

class TiketReguler(Tiket):
    def __init__(self, film, kursi, harga, bonus_air_mineral=True):
        super().__init__(film, kursi, harga)
        self.bonus_air_mineral = bonus_air_mineral

    def cetak(self):
        super().cetak()
        if self.bonus_air_mineral:
            print("Dapat bonus air mineral gratis")

class TiketVip(Tiket):
    biaya_vip = 25000

    def __init__(self, film, kursi, harga, nomor_sofa):
        super().__init__(film, kursi, harga)
        self.nomor_sofa = nomor_sofa
    def total_harga(self):
        total_biasa = super().total_harga()
        return total_biasa + TiketVip.biaya_vip

    def cetak(self):
        super().cetak()
        print("Sofa nomor:", self.nomor_sofa, "| Biaya tambahan VIP:", TiketVip.biaya_vip)


class Transaksi:
    diskon_member = 0.1

    def __init__(self, member=False):
        self.member = member
        self.__list_tiket = []

    def tambah(self, tiket):
        self.__list_tiket.append(tiket)
        print("Tiket", tiket.film.judul, "sudah ditambahkan")

    def bayar(self):
        total = 0
        for t in self.__list_tiket:
            total += t.total_harga()
        if self.member:
            total = total - (total * Transaksi.diskon_member)
        return total

    def struk(self):
        print("STRUK PEMBAYARAN")
        for t in self.__list_tiket:
            t.cetak()
        status = "Member" if self.member else "Umum"
        print("Status:", status)
        print("Total Bayar:", self.bayar())

    def cetak_struk_fisik(self, mesin):
        isi = f"Struk a.n. {'Member' if self.member else 'Umum'}, total Rp{self.bayar():,.0f}"
        mesin.cetak(isi)

    @classmethod
    def atur_diskon(cls, diskon_baru):
        cls.diskon_member = diskon_baru
        print("Diskon member sekarang jadi", diskon_baru * 100, "%")

print("CLASS FILM")
film1 = Film("Avengers: Doomsday", "Action", 150)
film2 = Film("Spider-Man: Brand New Day", "Action", 130)
film1.tampilkan()
film2.tampilkan()

print("\nSUBCLASS TIKET REGULER & VIP")
tiket1 = TiketVip(film1, "A1", 85000, nomor_sofa="S1")
tiket2 = TiketReguler(film2, "B5", 35000)
tiket1.cetak()
print()
tiket2.cetak()

print("\nCEK ISINSTANCE DAN ISSUBCLASS")
print("tiket1 termasuk Tiket?", isinstance(tiket1, Tiket))
print("TiketVip subclass dari Tiket?", issubclass(TiketVip, Tiket))

print("\nSETTER HARGA (lewat superclass)")
tiket1.harga = 90000
print("Harga tiket1 setelah diubah:", tiket1.harga)
tiket1.harga = -5000
print("Harga tiket1 setelah dicoba minus:", tiket1.harga)

print("\nCLASS TRANSAKSI (AGREGASI)")
transaksi1 = Transaksi(member=True)
transaksi2 = Transaksi(member=False)

transaksi1.tambah(tiket1)
transaksi1.tambah(tiket2)
transaksi1.struk()

transaksi2.tambah(tiket2)
transaksi2.struk()

print("\nCLASS METHOD atur_diskon")
Transaksi.atur_diskon(0.2)
transaksi1.struk()

print("\nASOSIASI: MESIN CETAK")
mesin_kasir = MesinCetak("Printer Kasir 1")
transaksi1.cetak_struk_fisik(mesin_kasir)