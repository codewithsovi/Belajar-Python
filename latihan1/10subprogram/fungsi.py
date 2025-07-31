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

# var-keyword(variadic keyword parameter) = menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi.
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ","
    return info

print(cetak_info(nama="sovi", umur="17", pekerjaan="programmer"))

# fungsi anonim(lambda expression) = fungsi tanpa mendeklarasikan def
# name_func = lambda args : ret_val
luas_persegi = lambda panjang, lebar: panjang*lebar
print(luas_persegi(4, 5))

# variable lokal yang di definisikan di dalam function sedangkan lgobal sebaliknya
