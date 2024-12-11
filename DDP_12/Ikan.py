from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenis, lamaHidup):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenis = jenis
        self.lamaHidup = lamaHidup

    def cetakIkan(self):
        super().cetak()
        print(f"Jenis \t\t: ", self.jenis, "\nLama Hidup \t: ", self.lamaHidup)

print("===========Hiu===========")
Hiu = Ikan("Hiu", "Ikan kecil", "Laut", "Bertelur dan Beranak", "Predator", "300 Tahun")
Hiu.cetakIkan()
print("==========Mujair==========")
Mujair = Ikan("Mujair", "Pelet", "Sungai", "Bertelur", "Bukan Predator", "10 Tahun")
Mujair.cetakIkan()