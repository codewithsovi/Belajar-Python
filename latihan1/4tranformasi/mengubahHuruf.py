# 1. upper() = mengubah huruf kecil >> besar
nama = "sovi"
nama = nama.upper()
print(nama)

# 2. lower() = mengubah huruf besar >> kecil
nama = "ALFI"
nama = nama.upper()
print(nama)

# 3. rstrip() = menghapus whitespace sebelah kanan
print("sovi     ".rstrip())

# 4. lstrip() = menghapus whitespace sebelah kanan
print("           Dicoding".lstrip())

# 5. strip() = menghapus whitespace kanan dan kiri
print("         alfi          ".strip())
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

"""
6. startswith() = untuk menentukan apakah benar kata pertama
secara penulisan harus benar (huruf kecil atau besarnya)
(jawabannya true or false)
"""
print("Sovi alfi nafilah".startswith('Sovi'))

# 7. endswith() = menentukan apakah kata akhir
print('Sovi Alfi Nafilah'.endswith('Nafilah'))
