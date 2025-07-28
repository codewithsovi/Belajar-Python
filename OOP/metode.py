# metode dari objek (object method)
class mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan +=10

mobil1 = mobil("kuning", "toyota", 100)
print(mobil1.kecepatan)

mobil1.tambah_kecepatan() #fungsi tambah_kecepatan
print(mobil1.kecepatan)

# metode static method
