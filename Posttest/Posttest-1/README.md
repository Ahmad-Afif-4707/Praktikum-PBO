# Sistem Pemesanan Tiket Bioskop CGV

## Tentang Program

Posttest ini mengguanakan tema sistem pemesanan tiket bioskop CGV, dibuat dengan Python menggunakan pendekatan Pemrograman Berorientasi Objek (PBO). Tema film yang dipakai adalah film-film Marvel seperti Avengers dan Spider-Man, dipilih karena sesuai dengan minat pribadi, dan tema ini sudah mendapat persetujuan dari aslab kelas.

Program ini terdiri dari tiga class yang saling berhubungan lewat objek, yaitu `Film`, `Tiket`, dan `Transaksi`. Ketiganya belum menggunakan pewarisan (inheritance) karena materi tersebut memang belum dipelajari, jadi rencananya akan ditambahkan sedikit-sedikit di posttest-posttest berikutnya. Fokus utama di tahap ini ada pada penerapan class, object, atribut, method, dan encapsulation sesuai tiga modul awal yang sudah dipelajari.

Alur programnya kurang lebih begini: objek film dibuat lebih dulu dari class `Film`, lalu dipakai untuk membuat objek tiket dari class `Tiket`, dan pada akhirnya tiket-tiket tersebut dikumpulkan ke dalam objek `Transaksi` untuk dihitung totalnya sekaligus dicetak struknya.

## Yang Dikerjakan

### 1. Membuat Class Film

Class `Film` dibuat untuk menyimpan data film yang akan ditonton. Bagian ini masih tergolong sederhana, hanya berisi atribut instance dan satu method saja, karena fungsinya memang sebatas menyimpan data.

- Atribut instance: `judul`, `genre`, `durasi`. Ketiganya diisi lewat `__init__()` menggunakan `self`, sehingga tiap objek film bisa punya nilai yang berbeda-beda.
- Method: `tampilkan()`, instance method yang dipakai untuk mencetak info film (judul, genre, durasi) ke layar.

### 2. Membuat Class Tiket

Class `Tiket` merepresentasikan satu tiket yang dipesan, dan dibuat berelasi dengan objek Film — jadi tiap tiket otomatis membawa objek film di dalamnya.

- Atribut kelas: `nama_bioskop` (isinya "CGV") dan `pajak` (isinya 0.11, untuk PPN 11%). Keduanya dijadikan atribut kelas karena nilainya sama untuk semua tiket, tidak perlu beda-beda tiap objek.
- Atribut instance: `film`, `jenis`, `kursi`, dan `__harga`. Khusus `__harga` dibuat private (dua underscore) karena harga dianggap sebagai data penting yang sebaiknya tidak bisa diubah sembarangan dari luar class.
- Decorator `@property` diterapkan pada `harga` sebagai getter, sehingga nilainya tetap bisa dibaca dari luar tapi melalui jalur yang terkontrol. Setter-nya (`@harga.setter`) dilengkapi validasi: kalau harga baru yang dimasukkan bernilai 0 atau minus, perubahan itu ditolak dan program mencetak pesan peringatan.
- Method instance: `total_harga()` untuk menghitung harga tiket setelah ditambah pajak, dan `cetak()` untuk menampilkan detail tiket (judul film, jenis, kursi, harga, total setelah pajak).
- Static method: `cek_jenis()`, dipakai untuk mengecek apakah jenis tiket yang dimasukkan termasuk yang tersedia (reguler, 3d, vip). Dijadikan static method karena fungsi ini tidak membutuhkan data dari objek maupun class-nya, cukup mengecek input saja.

### 3. Membuat Class Transaksi

Class `Transaksi` menangani proses pembelian, di mana satu transaksi bisa berisi lebih dari satu tiket sekaligus.

- Atribut kelas: `diskon_member` (isinya 0.1, diskon 10% untuk pelanggan member).
- Atribut instance: `member` (status apakah pembeli member atau bukan) dan `__list_tiket` (daftar tiket yang dibeli dalam transaksi tersebut). `__list_tiket` dibuat private karena daftar ini idealnya hanya bisa diubah lewat method yang sudah disediakan, bukan diubah langsung dari luar.
- Method instance: `tambah()` untuk memasukkan objek tiket ke dalam `__list_tiket`, `bayar()` untuk menjumlahkan total harga semua tiket dan otomatis mengurangi diskon kalau pembelinya member, serta `struk()` untuk mencetak ringkasan seluruh transaksi (daftar tiket, status member, total bayar).
- Class method: `atur_diskon()`, menggunakan `@classmethod` supaya method ini bisa mengubah nilai `diskon_member` dan perubahannya langsung berlaku untuk semua objek Transaksi yang ada, bukan cuma satu objek saja.

### 4. Menerapkan Encapsulation

Dua atribut dibuat private dalam program ini, yaitu `__harga` di class Tiket dan `__list_tiket` di class Transaksi. Keduanya dianggap sebagai data penting, sehingga tidak seharusnya bisa diubah sembarangan langsung dari luar class tanpa melalui validasi.

Untuk `__harga`, getter dan setter dibuat memakai decorator `@property` dan `@harga.setter`, dengan validasi di dalam setter-nya: kalau ada percobaan mengisi harga dengan angka 0 atau minus, program akan menolak perubahan tersebut dan mencetak pesan peringatan, bukan langsung mengubah nilainya begitu saja.

### 5. Melakukan Pengujian Program

Bagian akhir program (main program) berisi beberapa pengujian, di antaranya:

- Dua objek film (Avengers: Doomsday dan Spider-Man: Brand New Day) dibuat untuk menguji class `Film` dan method `tampilkan()`.
- Dua objek tiket dengan jenis dan harga berbeda dibuat untuk menguji class `Tiket`, sekaligus mencoba method `cetak()` dan `total_harga()`.
- Static method `cek_jenis()` diuji dengan dua input, satu valid ("vip") dan satu tidak valid ("gold"), untuk membuktikan fungsi ini bekerja sesuai harapan.
- Setter `harga` diuji dengan dua kondisi: mengisi angka valid (90000) yang seharusnya diterima, dan mengisi angka minus (-5000) yang seharusnya ditolak. Dari pengujian ini terbukti validasi yang dibuat benar-benar berjalan.
- Dua objek transaksi dibuat, satu untuk pembeli member dan satu untuk pembeli umum, lalu method `tambah()`, `bayar()`, dan `struk()` diuji di masing-masing objek untuk memastikan perhitungan diskon berjalan sesuai status membernya.
- Class method `atur_diskon()` turut diuji dengan mengubah diskon member dari 10% menjadi 20%, kemudian struk dicetak ulang untuk membuktikan perubahan itu berlaku ke seluruh objek Transaksi.
