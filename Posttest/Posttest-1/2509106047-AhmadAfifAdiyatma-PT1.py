class Film:
    def __init__(self, judul, genre, durasi):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi

    def tampilkan(self):
        print(self.judul, "-", self.genre, "-", self.durasi, "menit")


class Tiket:
    nama_bioskop = "CGV"
    pajak = 0.11

    def __init__(self, film, jenis, kursi, harga):
        self.film = film
        self.jenis = jenis
        self.kursi = kursi
        self.__harga = harga

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            print("Harga gak boleh 0 atau minus")
        else:
            self.__harga = harga_baru

    def total_harga(self):
        return self.__harga + (self.__harga * Tiket.pajak)

    def cetak(self):
        print(self.film.judul, "-", self.jenis, "- Kursi", self.kursi)
        print("Harga:", self.__harga, "| Total dengan pajak:", self.total_harga())

    @staticmethod
    def cek_jenis(jenis):
        jenis_tersedia = ["reguler", "3d", "vip"]
        return jenis.lower() in jenis_tersedia


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

    @classmethod
    def atur_diskon(cls, diskon_baru):
        cls.diskon_member = diskon_baru
        print("Diskon member sekarang jadi", diskon_baru * 100, "%")


print("CLASS FILM")
film1 = Film("Avengers: Doomsday", "Action", 150)
film2 = Film("Spider-Man: Brand New Day", "Action", 130)
film1.tampilkan()
film2.tampilkan()

print("\nCLASS TIKET")
tiket1 = Tiket(film1, "vip", "A1", 85000)
tiket2 = Tiket(film2, "reguler", "B5", 35000)
tiket1.cetak()
tiket2.cetak()

print("\nSTATIC METHOD cek_jenis")
print("Cek 'vip' :", Tiket.cek_jenis("vip"))
print("Cek 'gold':", Tiket.cek_jenis("gold"))

print("\nSETTER HARGA")
tiket1.harga = 90000
print("Harga tiket1 setelah diubah:", tiket1.harga)
tiket1.harga = -5000
print("Harga tiket1 setelah dicoba minus:", tiket1.harga)

print("\nCLASS TRANSAKSI")
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