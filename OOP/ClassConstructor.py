# functio di dalam class
class mobil:
    # atribut instance
    def __init__(self, warna, merek):
        self.warna = warna
        self.merek = merek

mobil1 = mobil("merah", "toyota")
mobil2 = mobil("kuning", "honda")

print(mobil1.warna)
print(mobil1.merek)
print(mobil2.warna)
print(mobil2.merek)

# method didalam class (class method)
