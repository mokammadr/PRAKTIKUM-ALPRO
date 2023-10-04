nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))

rata_rata = (uts + uas) / 2

if rata_rata >= 100:
    nilai_huruf = 'A'
elif rata_rata >= 80:
    nilai_huruf = 'B'
elif rata_rata >= 70:
    nilai_huruf = 'C'
elif rata_rata >= 40:
    nilai_huruf = 'D'
else:
    nilai_huruf = 'E'
print("Nama:", nama)
print("NIM:", nim)
print("Nilai rata-rata:", rata_rata)
print("Nilai huruf:",nilai_huruf)