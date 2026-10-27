# class AkunBank:
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

#     def hitung_bunga(self):
#         return 0

# class Tabungan(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.02


# class Deposito(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.06

# # Polimorfisme: Satu Loop, perilaku berbeda
# daftar_akun = [Tabungan("Budi", 1000000), Deposito("Sari", 5000000)]
# for akun in daftar_akun:
#     print(f"Bunga {akun.nama}: Rp {akun.hitung_bunga():,.2f}")

#-----------------------------------------------------------------------------
# class RekeningTabungan:
#     def __init__(self, saldo):
#         self.saldo = saldo

#     def tarik_uang(self, jumlah):
#         if jumlah <= self.saldo:
#             self.saldo -= jumlah
#             print(f"Penarikan Rp {jumlah:,} berhasil.")
#             print(f"Saldo tersisa: Rp {self.saldo:,}")
#         else:
#             print("Saldo tidak cukup.")


# class RekeningGiro:
#     def __init__(self, saldo):
#         self.saldo = saldo

#     def tarik_uang(self, jumlah):
#         if jumlah <= self.saldo:
#             self.saldo -= jumlah
#         else:
#             print("Saldo tidak cukup.")


# # Duck typing
# def proses_penarikan(rekening, jumlah):
#     rekening.tarik_uang(jumlah)


# tabungan = RekeningTabungan(5_000_000)
# giro = RekeningGiro(10_000_000)

# proses_penarikan(tabungan, 1_000_000)
# proses_penarikan(giro, 2_000_000)

# # Output:
# # Penarikan Rp 1,000,000 berhasil.
# # Saldo tersisa: Rp 4,000,000
# # Penarikan Rp 2,000,000 dari rekening giro berhasil.
# # Saldo tersisa: Rp 8,000,000

from abc import ABC, abstractmethod


class Transaksi(ABC):
    @abstractmethod
    def validasi(self):
        """Wajib diimplementasikan oleh kelas anak."""
        pass

    @abstractmethod
    def eksekusi(self):
        """Wajib diimplementasikan oleh kelas anak."""
        pass


class TarikTunai(Transaksi):
    def __init__(self, saldo_akun, nominal):
        self.saldo = saldo_akun
        self.nominal = nominal

    def validasi(self):
        if self.nominal > self.saldo:
            return False
        return True

    def eksekusi(self):
        if self.validasi():
            self.saldo -= self.nominal
            print(f"Tarik tunai berhasil. Sisa saldo: {self.saldo}")
        else:
            print("Saldo tidak cukup!")


class TransferGagal(Transaksi):
    def validasi(self):
        return True
    # Lupa implementasi eksekusi()!


transaksi_sukses = TarikTunai(100000, 50000)
transaksi_sukses.eksekusi()

try:
    transaksi_gagal = TransferGagal()
except TypeError as e:
    print(f"Error: {e}")