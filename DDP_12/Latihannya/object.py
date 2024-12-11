from mahasiswa import *
from dosen import *

#buat object
m1 = Mahasiswa("Siti Aminah", "Wanita", 20, "SI", 3)
m2 = Mahasiswa("Budi Santoso", "Pria", 23, "TI", 5)
d1 = Dosen("Sirojul Munir", "Pria", 43, "S.Si, M.Kom", "LPPM")
d2 = Dosen("Henry Saptono", "Pria", 44, "S.Si, M.Kom", "LTSI")

#gunakan fungsi2 yang ada di class
d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()