z = 0
try:
    print(1/z)
except ZeroDivisionError:
    print("anda tidak bisa membagi angka tersebut") # jadi pesan yang tampil bisa di custom


var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")


# raise >> 
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan") #menampilkan pesan error
else :
    for i in range(var):
        print(i+1)