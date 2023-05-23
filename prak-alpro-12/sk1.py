# bilangan unik sejumlah n

#input user
n = int(input('Masukkan n:'))
bilangan_input = set() # siapkan set kosong

# minta input n bilangan, langsung masukkan dalam set
for i in range(n):
    bilangan = int(input('Masukkan bilangan: '))
    bilangan_input.add(bilangan)

print(f'Bilangan unik yang anda masukkan adalah: {bilangan_input}')

# nilai tertinggi
print(f'Nilai max: {max(bilangan_input)}')

# nilai terkecil
print(f'Nilai min: {min(bilangan_input)}')

# len
print(f'Anda memiliki {len(bilangan_input)} bilangan unik')