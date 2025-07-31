# "super()" untuk mengambil metode tambah_kecepatan yang berasal dari super class atau induknya, yaitu kelas Mobil.
class mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


class mobil_sport(mobil):
    def turbo(self):
        self.kecepatan +=20
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("kecepatan anda meningkat")

# Kelas Mobil Sport
mobil_sport_1 = mobil_sport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)