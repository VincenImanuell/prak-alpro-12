aplikasi = {
    1: ['A', 'B', 'D', 'E', 'F'],
    2: ['B', 'D', 'G', 'B'],
    3: ['C', 'F', 'G', 'B']
}

set_aplikasi = []
for keys in aplikasi.keys():
    set_aplikasi.append(set(aplikasi[keys]))

print(set_aplikasi)

hasil = set_aplikasi[0] & set_aplikasi[1] & set_aplikasi[2]
semua_aplikasi = set_aplikasi[0] | set_aplikasi[1] | set_aplikasi[2]

print(f'Yang sama semua: {hasil}')
print(f'Semua aplikasi: {semua_aplikasi}')