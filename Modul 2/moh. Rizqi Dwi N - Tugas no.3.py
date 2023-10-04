# Informasi tentang Jaka
nama_jaka = "Jaka"
skor_jaka = 1100
ipk_jaka = 3.5

# Informasi tentang Ida
nama_ida = "Ida"
skor_ida = 1000
ipk_ida = 3.5

# Persyaratan beasiswa
skor_minimum = 1100
ipk_minimum = 3.0

# Menentukan siapa yang lulus persyaratan beasiswa
if skor_jaka > skor_minimum and ipk_jaka >= ipk_minimum:
    hasil_jaka = f"{nama_jaka} memenuhi persyaratan beasiswa."
else:
    hasil_jaka = f"{nama_jaka} tidak memenuhi persyaratan beasiswa."

if skor_ida > skor_minimum and ipk_ida >= ipk_minimum:
    hasil_ida = f"{nama_ida} memenuhi persyaratan beasiswa."
else:
    hasil_ida = f"{nama_ida} tidak memenuhi persyaratan beasiswa."

# Menampilkan hasil
print(hasil_jaka)
print(hasil_ida)
