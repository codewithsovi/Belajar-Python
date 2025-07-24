# sukensial array >> mencetak setiap elemen yang berada pada variabel array "var_arr" menggunakan perulangan loop. 

var_arr = [1, 2, 3, 4,5]
for i in range(len(var_arr)):
    current_element = var_arr[i] #metode indexing
    next_index = i+1 #suksesor indeks

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
    
    print(f"Current element: {current_element}, next elemnt : {next_element}")



# mencari element indeiks terbesar
var_arr = [1, 3, 65, 8, 9, 90]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

