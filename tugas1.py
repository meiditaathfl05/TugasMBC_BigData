print("## program python menghitung gaji karyawan")
print("---------------------------------------")
print("")

nama = input("nama karyawan: ")
golongan = input("golongan: ")
jamkerja = int(input("jumlah jam kerja: "))

print()

if golongan == "A":
  upah = 5000
elif golongan == "B":
  upah = 7000
elif golongan == "C":
  upah = 8000
elif golongan == "D":
  upah = 10000

total = jamkerja * upah

if (jamkerja - 48) > 0:
  total = total + ((jamkerja - 48)*4800)

#output
print(nama, "menerima upah Rp.", total, "per minggu")