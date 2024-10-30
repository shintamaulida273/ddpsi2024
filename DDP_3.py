# 1. buatlah program phyton untuk menuliskan profil prodi (nama,nim,kelas,no telp,alamat) menggunakan variabel dan di cetak (print)
nama = "Shinta Maulida Distiandini"
nim = "0110124201"
kelas = "Rombel 11"
no_telp = "089603260381"
alamat = "Kp. Sawah Rt 02 Rw 07 No. 46"
print('Jadi nama saya adalah', nama)
print(nim)
print(kelas)
print(no_telp)
print(alamat)

# 2. buat seperti no 1 tapi 1 nama teman kalian
nama = "Nadya Nurus Sakinah"
nim = "0110124196"
kelas = "Rombel 12"
no_telp = "085695307035"
alamat = "Perumahan Grahatama Indah 3 blok I No. 7"
print('Nama teman saya adalah', nama)
print(nim)
print(kelas)
print(no_telp)
print(alamat)

# 3. buat program phyton untuk mencari nilai berat badan ideal
Tb = int(input('Masukkan tinggi badan: '))
Bb_ideal = ((Tb - 100)-(Tb - 100) * 0.15)
print('jadi berat badan ideal saya adalah :',Bb_ideal)

# 4. buatlah program phyton untuk mencari nilai konversi dari celcius ke fahreinheit
# Rumus = (celcius * 9/5) + 32
celcius = int(input('masukkan celcius: '))
fahreinheit = (celcius * 9/5) + 32
print('jadi fahreinheit dari celcius itu adalah', fahreinheit)

# 5. buatlah program phyton untuk mencari luas dan keliling tabung
# input jari-jari dan tinggi
jari_jari = 3
tinggi = 8
pi = 3.14

#proses
luas_tabung = 2*pi*(jari_jari*jari_jari+tinggi)
keliling_tabung = 2*pi*tinggi

#output
print('luas tabung adalah', luas_tabung)
print('keliling tabung adalah', keliling_tabung)