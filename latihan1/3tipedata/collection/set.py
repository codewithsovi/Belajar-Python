# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection)
set = {1, 2, 3, 4, 4, 5}
print(type(set))

#nilai duplikat di dalamnya akan dihapus. 
print(set)

# set adalah himpunan dalam matematika. Ini maknanya Anda dapat melakukan operasi 
# union (gabungan) dan intersection (irisan) pada set.
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 4, 8}

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)
