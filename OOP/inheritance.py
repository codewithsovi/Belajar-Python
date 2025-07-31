# class utama
class mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

# class turunan
class mobil_sport(mobil):
    def turbo(self):
        self.kecepatan += 20


mobil1 = mobil("merah", "yamaha", 100)
print(mobil1.kecepatan)
mobil1.tambah_kecepatan()
print(mobil1.kecepatan)

mobil_sport1 = mobil_sport("hitam", "suzuki", 200)
print(mobil_sport1.kecepatan)
mobil_sport1.turbo()
print(mobil_sport1.kecepatan)