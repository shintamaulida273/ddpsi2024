#1 Bilangan Genap atau Ganjil
bilangan = int(input("masukkan bilangan :"))
if(bilangan % 2):
    print(f"{bilangan} adalah bilangan ganjil")
else:
    print(f"{bilangan} adalah bilangan genap")

#2 Nilai Ujian
nilaiujian = int(input("Masukkan Nilai Ujian :"))
if(nilaiujian >= 75):
    print("Anda Lulus, Congratss!!! OTW MAKAN-MAKAN!!")
else:
    print("Anda Tidak Lulus, Sangat Disayangkan Sekali")

#3 Cek Usia dan Status
usia = int(input("Masukkan usiamu :"))
if(usia >= 18):
    print("Kamu Sudah Dewasa Dik")
elif(usia >= 13 and usia <= 17):
    print("Kamu Masih Remaja")
elif(usia <= 12):
    print("Kamu Anak Kecil")

#4 Cek Keanggotaan
statuskeanggotaan = input("Masukkan Status Keanggotaan:")
if(statuskeanggotaan == "gold" or statuskeanggotaan == "silver"):
    print("Selamat! Anda Dapat Diskon")
elif(statuskeanggotaan == "bronze"):
    print("Anda Tidak Dapat Diskon")
else:
    print("Imputan Yang Anda Masukkan Tidak Valid")

#5 Pembelian Diskon
pembelian = float(input("Masukkan Jumlah Pembelian Anda :"))
print(f"Dapat Diskon 10%") if pembelian > 100.000 else print("Tidak Dapat Diskon")