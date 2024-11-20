#1 Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0
print('\n----- mencari celcius ke fahrenheit-----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
#untuk mencetak value
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#2 Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False
print('\n----- mencari bilangan genap-----')
def is_genap(bil_genap):
    return bil_genap %2 == 0
#untuk mencetak value
print(is_genap(4))
print(is_genap(7))

#3 Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai (60) #gagal
print('\n----- mencari keterangan lulus-----')
def nilai(jumlah):
    if jumlah >= 80:
        return 'Lulus'
    else:
        return 'Tidak Lulus'
#untuk mencetak value
print(nilai(80))
print(nilai(60))

#4 Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19
print('\n----- mencari angka ganjil-----')
def ganjil(angka):
    for i in range (1,angka, 2):
        print(i, end=" ")
#untuk mencetak value  
ganjil(20)