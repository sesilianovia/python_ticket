def main():
  # Daftar harga sewa
  harga_sewa = {
    "Sepeda": 10000,
    "Motor": 25000,
    "Mobil": 50000,
    "Elf": 100000,
    "Bis": 200000,
  }

  # Daftar daerah di sekitar Yogyakarta
  daerah_yogyakarta = {
    "Malioboro",
    "Ujung Kulon",
    "Parangtritis",
    "Srandakan",
    "Prambanan",
  }

  # Mendapatkan data peminjaman
  tujuan = input("Masukkan tujuan: ")
  if tujuan not in daerah_yogyakarta:
    print("Mohon maaf, tujuan yang Anda pilih tidak tersedia")
    return

  nama = input("Masukkan nama: ")
  kendaraan = input("Masukkan kendaraan: ")
  jam_peminjaman = int(input("Masukkan jam peminjaman: "))

  # Periksa apakah kendaraan tersedia
  if kendaraan not in harga_sewa:
    print("Mohon maaf kendaraan yang Anda pilih tidak tersedia")
    return

  # Hitung harga per jam
  biaya_tambahan = 50000
  harga_per_jam = harga_sewa[kendaraan] + biaya_tambahan

  # Hitung total biaya
  total_biaya = harga_per_jam * jam_peminjaman

  # Tampilkan hasil
  print("Tujuan:", tujuan)
  print("Nama:", nama)
  print("Kendaraan:", kendaraan)
  print("Jam peminjaman:", jam_peminjaman)
  print("Harga per jam:", harga_per_jam)
  print("Total biaya:", total_biaya)

if __name__ == "__main__":
  main()
