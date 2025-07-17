# 1. zfill() = menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu.
nama = 'sovi'
tambah = nama.zfill(6)

# 2. rjust() = menambahkan apa saja tidak hanya whitespace. (rata kanan)
print('dicoding'.rjust(20))
print('dicoding'.rjust(10))

print('sovi'.rjust(10, '!'))

# ljust() = menambahkan apa saja tidak hanya whitespace. (rata kiri)
print('sovi'.ljust(10, '!'))

# center() = rata kanan kiri
print('sovi'.center(10, '-'))
