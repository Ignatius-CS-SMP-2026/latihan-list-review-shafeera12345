# NAMA  : Shafeera Renata Ibrahim
# KELAS : 9B
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
data_nilai_asli = [75, 55, 90, 45, 95, 80]
print("Data nilai asli: ", data_nilai_asli)
data_nilai_asli.sort(reverse=True)
print("Data setelah diurutkan (Descending): ", data_nilai_asli)
tiga_nilai_tertinggi = data_nilai_asli[:3]
print("Tiga nilai tertinggi (Penerima Beasiswa): ", tiga_nilai_tertinggi)
daftar_nilai_yang_lulus = []
for nilai in data_nilai_asli:
    if nilai >= 60:
        daftar_nilai_yang_lulus.append(nilai)
print("Daftar nilai yang lulus: ", daftar_nilai_yang_lulus)