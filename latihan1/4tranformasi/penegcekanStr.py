# ertujuan untuk melakukan pengecekan pada string. Hasil dari kategori ini adalah mengembalikan nilai boolean True/False. 

# 1. isupper() = Apakah kapital?
nama = "SOVI"
print(nama.isupper())

# 2. islower() =  apakah hurudf kecil?
nama = 'sovi'
print(nama.islower())

# 3. isalpha() = Apakah semua huruf alphabeth
nama = "alfi"
print(nama.isalpha())

# 4. isalnum() = true jika terdiri dari alphabeth dan numeric
nama = "sovi123"
print(nama.isalnum())

# 5. isdecimal() = True jika karakter dalam string berisi hanya angka/numerik.
print('123'.isdecimal())

# 6. isspace() = jika string hanya berisi whitespace
print('     '.isspace())

# 7. istitle() = True jika string berisi huruf kapital pada setiap kata pertamanya.
print("Sovi Alfi Nafilah".istitle())
