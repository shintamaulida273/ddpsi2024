from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, design, racun):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.design = design
        self.racun = racun

    def cetakUlar(self):
        super().cetak()
        print(f"Design \t\t: ", self.design, "\nRacun \t\t: ", self.racun)

print("==========Anaconda==========")
Anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur dan Beranak", "Polkadot", "Tidak Beracun")
Anaconda.cetakUlar()
print("===========Kobra===========")
Kobra = Ular("Kobra", "Kancil", "Semak-Semak", "Bertelur", "Polos", "Beracun")
Kobra.cetakUlar()