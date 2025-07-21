"""
Ternary operators dibangun dengan menempatkan "blok kode jika benar"
pada posisi awal, lalu diikuti oleh "if statement" serta "kondisi"-nya. 
Kemudian "else statement" ditempatkan di akhir beserta dengan "blok kode jika salah".
"""

lulus = True
print("selamat anda lulus") if lulus else print("perbaiki")

# Ternary Tuples >> (blok kode salah, blok kode)[kondisi]
lulus = True
kelulusan = ("anda tidak lulus", "anda lulus")[lulus]
print(kelulusan)

