# Input umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# Penyeleksian kondisi untuk menentukan kategori umur
if umur > 50:
    kategori = "Tua"
elif umur > 25:
    kategori = "Muda"
elif umur > 17:
    kategori = "Dewasa"
elif umur > 7:
    kategori = "Anak-anak"
else:
    kategori = "Balita atau di bawah 7 tahun"

# Menampilkan hasil kategori umur
print(f"Anda termasuk dalam kategori: {kategori}")
