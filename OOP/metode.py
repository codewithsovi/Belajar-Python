# 1. metode dari objek (object method)
class mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self): #object methode
        self.kecepatan +=10

mobil1 = mobil("kuning", "toyota", 100)
print(mobil1.kecepatan)

mobil1.tambah_kecepatan() #fungsi tambah_kecepatan
print(mobil1.kecepatan)

# 2. metode static @staticmethod
class mobil:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("ini adalah penggunaan methode static")

# pemanggilan dengan objek
mobil.intro_mobil()

# pemanggiulan dengan objek
mobil1 = mobil("dicodingcar")
mobil1.intro_mobil()


# 3. class method @classmethod
class motor:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro(cls):
        print("ini adalah penggunaan kelas method")

motor.intro()

motor2 = motor("yamaha")
motor2.intro()