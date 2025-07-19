# 1. len() >> bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.
# pada list
contoh = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
print("panjang dari list : \t", len(contoh))

# pada set
contoh = set([1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8])
print("panjang dari set : \t",len(contoh))

# pada string
contoh = "saya adalah mahasiswa"
print("panjang dari string : \t",len(contoh))

# 2. min() dan max() >> untuk mengetahui berapa nilai minimum dan maksimum dari suatu list 
angka = [4, 2, 3, 4, 5, 8, 8, 8 , 10, 1]
print("angka terkecil : \t",min(angka))
print("angka terbesar : \t",max(angka))

# 3. count() >> untuk mengetahui berapa kali suatu objek muncul dalam list
angka = [1, 1, 2, 3, 4, 5, 7, 7, 7, 7, 8]
print("Banyaknya 1 muncul : \t",angka.count(1))

# pada string 
string = "nama saya sovi alfi nafilah"
substring = "a"

print("Banyaknya A muncul: \t",string.count(substring))


# 4. In dan Not In >> diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list.
kalimat = "nama saya sovi alfi nafilah"
print(kalimat)
print("Apakah ada kata sovi? ", 'sovi' in kalimat)
print("Apakah ada kata sovi? ", 'sovi' in kalimat)
print("Apakah tdk ada kata nama? ", 'nama' not in kalimat)
print("Apakah tdk ada kata dea? ", 'dea' not in kalimat)

# 5. memberikan nilai untuk multiple variable
data =['shirt', 'white', 'l']
apparel = data[0] # mengambil value kemudian memasukkannya ke variable
color = data[1]
size = data[2]
print(color)

# dapat melakukannya skaligus
data1 =['kemeja', 'putih', 'xl']
apparel, warna, ukuran = data1 #jumlah variable == jumlah value
print(warna)

# 6. sort() >> mengurutkan angka atau urutan huruf.
nama = ['sovi', 'alfi', 'nafilah']
nama.sort()
print(nama)

# reverse = true
nama = ['sovi', 'alfi', 'nafilah']
nama.sort(reverse=True)
print(nama)

# tidak dapat melakukan sort jika datanya terdapat string dan angka dalam 1 ser/list
# urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)