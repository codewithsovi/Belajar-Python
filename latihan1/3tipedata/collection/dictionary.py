# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan
# terdiri dari key : value
x ={'nama':'sovi', 'umur':17, 'jenis kelamin':'perempuan', 'indonesia':True}
print(type(x))

# indexing
print("nama", x['nama'], "RI", x['indonesia']) 
print(x['umur']) 

# menambahkan data pada dictionary
x['job'] = "Programmer"
print(x)

# Menghapus Data pada Dictionary
del x['job']
print(x)

# Mengubah Data pada Dictionary
x['nama'] = "Alfi"
print(x)