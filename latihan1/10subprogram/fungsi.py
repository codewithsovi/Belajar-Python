def luas_persegi_panjang(panjang, lebar): #function header
    luas = panjang * lebar #function body
    print("hasilnya adalah :", luas)
    return luas #function return
luas_persegi_panjang(20, 30)

luas_persegi_panjang(40, 30)

# dinamis
def persegi(p, l):
    luas = p* l
    return luas

p = int(input("masukkan panjang persegi : "))
l = int(input("masukkan panjang luas : "))

persegi3 = persegi(p,l)
print(persegi3)

# args = bisa memasukkan angka sebanyak apa pun dalam argumen fungsi.

def hitungTotal(*args):
    print(type(args))
    total =sum(args)
    return total

print(hitungTotal(1, 2, 3))