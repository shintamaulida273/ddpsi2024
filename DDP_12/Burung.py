from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, bunyi, warna):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.bunyi = bunyi
        self.warna = warna

    def cetakBurung(self):
        super().cetak()
        print(f"Bunyi \t\t: ", self.bunyi, "\nJenis \t\t: ", self.warna)

print("==========Gagak==========")
Gagak = Burung("Gagak", "Anak Ayam", "Hutan", "Bertelur", "Ngak Ngak", "Hitam")
Gagak.cetakBurung()
print("==========Merak==========")
Merak = Burung("Merak", "Biji-bijian", "Kebun", "Bertelur", "Waw Waw", "Hijau")
Merak.cetakBurung()