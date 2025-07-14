
# double qoute
kalimat = """
Penggunaan tiga single qoute untuk
kalimat yang memiliki efek Enter
"""
print(kalimat)

# string merupakan urutan karakter
x = 'sovi'
print(x[0])

# mengakses substring
x = 'soviAlfi'
# string

# menyisakan 2 karakter didepan
print(x[:2])
# menghilangkan 2 karakter didepan
print(x[2:])

# formated string (menyisipkan variable pada string)
name = 'sovi'
print(f"hai, nama saya{name} dan saya berumur 17th")

namaPanjang = 'alfi'
print("Nama saya sovi %s" % (namaPanjang))

namaLengkap = 'sovi alfi nafilah'
print("Nama saya {}".format(namaLengkap))

#mengubah huruf besar dan kecil (upper dan lower)
kata = 'sovi'
kata = kata.upper()
print(kata)

kata = 'ALFI'
kata = kata.lower()
print(kata)

# Awalan dan Akhiran whitespace (menghilangkan kata yang tidak diinginkan)
print("sovi     ".rstrip())
print("           Dicoding".lstrip())
print("         alfi          ".strip())

 