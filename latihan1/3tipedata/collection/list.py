# List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, sedangkan array sebaliknya.

variable_list = [1, 'sovi', True, 2.0]

print(variable_list)
print(variable_list[2])

# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
x[0] = 1
print(x)

# indexing
y = ["laptop", "handphone", "senter", "sound", "keyboard", "webcam"]
print(y[3])
# indeks ke-3 dari terakhir
print(y[-3])

# pengambilan data berdasarkan sequence (slicing)
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

# sequence[start:stop:step]
print(x[0:5:2])
print(x[1:])
print(x[:3])



