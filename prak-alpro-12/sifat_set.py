# set mirip seperti himpunan
# set ketika di-add maka akan dimasukkan secara random tempatnya
a = {2, 4, 6, 8, 10, 12}
a.add(14)
print(a)
a.add(20)
print(a)

# pop() hapus isi random
# discard() hapus 1 tidak error jika tidak ada di set
# remove() hapus 1, jika tidak ada akan error
# clear() hapus semua

b = {2, 4, 6, 8, 10, 12}
old = 8
new = 18
if old in b:
    b.remove(old)
    b.add(new)
b1 = list(b)
print(b1)

# menghilangkan duplikat
c = [1, 2, 2, 4, 5, 5, 5]
c1 = set(c)
c2 = list(c1)
print(c2)
