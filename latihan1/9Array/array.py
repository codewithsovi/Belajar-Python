import array

x = array.array("i", [1, 2, 3, 4])
print(x)
print(type(x))

# nilai default pada array
# nama array = [default_val for in range(panjang array)]

var_arr = [0 for i in range(10)]
print(var_arr)
print(type(var_arr))

# untuk mengubah nilainya
for i in range(10):
    var_arr[i] = i

print(var_arr)

# mengakses array
print(var_arr[1])