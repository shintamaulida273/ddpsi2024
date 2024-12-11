class Animal:
    def __init__ (self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan 
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print(f"Nama \t\t: ", self.nama, "\nMakanan \t: ", self.makanan, "\nHidup \t\t: ", self.hidup, "\nBerkembang Biak : ", self.berkembangBiak)


