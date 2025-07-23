# 1. penggunaan break >> menghentikan program
for i in range(2):
    print("perulangan luar : ", i)
    for j in range(10):
        print("perulangan dalam : ", j)
        if j == 1:
            break


# 2. penggunaan continue >> melewati statement lalu lanjut 
for huruf in 'dico ding':
    if huruf == ' ':
        continue
    print('huruf saat ini : {}'.format(huruf))

# 3. else setelah for >> memberikan jalan keluar program saat pencarian tidak ditemukan.
numbers = [1, 2, 3, 4, 4, 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! program berhenti")
        break
else:
    print("Angka tidak ditemukan")

# 4. else setelah while >> blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. 
count = 0

while count < 3 :
    print("Dicoding Indonesia")
    count += 1

else:
    print("Blok dieksekusi karena kondisi salah")


# 5. Pass >> tindakan yang tidak ada apa-apanya
x = 10

if x < 5:
    pass
else:
    print("nilai x tidak memenuhi")


# 6. list comprehension >> membuat sebuah list baru berdasarkan list yang sudah ada.
angka = [1, 2, 3, 4]
pangkat =[]
for n in angka:
    pangkat.append(n**2) #untuk menambahkan nilai baru ke dalam variabel "pangkat"
print(pangkat)

# bisa menggunakan cara yang lebih mudah yaitu:
# new = [expresion for conditions]
number = [1, 2, 3, 4]
pangkat = [n**2 for n in number]
print(pangkat)