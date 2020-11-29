#membuka dan mau membaca file d:/data.txt
try:
    file = open ("c:/data.txt", "r")
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)

#jika error, munculkan exception !
except FileNotFoundError:
    print('file tidak ditemukan')
