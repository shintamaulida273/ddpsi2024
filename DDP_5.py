#NO 1
kendaraan = ["mio","motor","200cc","hitam","roda 2"]
kendaraan.append ("20.000.000")
kendaraan.append ("matic")
print(kendaraan)
kendaraan.insert (2, "yamaha")
print(kendaraan)

#NO 2
pilihan = input("""pilih nomor pilihan:
                1. Menghitung luas persegi
                2. Menghitung luas lingkaran
                3. Menghitung luas segitiga
                """)
                
match pilihan:
    case "1":
        print("menghitung luas persegi")
        s=int(input("Masukkan nilai sisi: "))
        luaspersegi = s * s
        print(f"luas persegi dengan sisi {s} adalah {luaspersegi}")
    case "2":
        print("menghitung luas lingkaran")
        pi = 3.14
        r = int(input("masukkan nilai jari-jari: "))
        luaslingkaran = pi * r**2
        print(f"luas lingkaran dengan sisi {r} adalah {luaslingkaran}")
    case "3":
        print("menghitung luas segitiga")
        alas = int(input("masukkan nilai alas: "))
        tinggi = int(input("masukkan nilai tinggi: "))
        luassegitiga = 1/2 * alas * tinggi
        print(f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luassegitiga}")
    case _:
        print("Input tidak valid")