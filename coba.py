import sys

list_version = [i for i in range(100000)]
gen_version = (i for i in range(100000))  # generator expression, mirip list comprehension tapi pakai ()

print(sys.getsizeof(list_version))  # ukuran memory list
print(sys.getsizeof(gen_version))   # ukuran memory generator — jauh lebih kecil!