# function didalam class
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
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("hello world!")

say_hello()

