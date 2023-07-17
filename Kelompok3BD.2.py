print(" ## Program Python Menghitung Gaji Karyawan ## ")
print("===================================================")
print("")

Nama = input("Nama Karyawan : ")
Gol = input("Golongan : ")
Jml = int(input("Jumlah jam kerja : "))


A = 5000
B = 7000
C = 8000
D = 10000

if Gol == 'A' and Jml > 48: 
  print(" ", Nama , "menerima upah Rp. ", (A*Jml + (Jml-48)*4000), "per minggu")
elif Gol == 'A' and Jml <= 48 :
  print(" ", Nama , "menerima upah Rp." , (A*Jml) , "per minggu")
elif Gol == 'B' and Jml > 48 :
   print(" ", Nama , "menerima upah Rp. ", (B*Jml + (Jml-48)*4000), "per minggu")
elif Gol == 'B' and Jml <= 48 : 
  print(" ", Nama , "menerima upah Rp." , (B*Jml) , "per minggu")
elif Gol == 'C' and Jml > 48 :
  print(" ", Nama , "menerima upah Rp. ", (C*Jml + (Jml-48)*4000), "per minggu")
elif Gol == 'C' and Jml <= 48 :
  print(" ", Nama , "menerima upah Rp." , (C*Jml) , "per minggu")
else :
  print ("Data tidak ditemukan")