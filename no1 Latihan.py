#membuka dan membaca file
try :
    file = input ("Silakan masukkan nama file yang ingin anda cari : ")
    bukaFile = open(file, "r")
    print('\n')
    print("Berikut isi file yang anda cari :")
    print('\n')
    print("-----------------------------")
    print('\n')
    print(bukaFile.read())

#jika file tidak terbaca, maka jalankan exception ini
except (FileNotFoundError):
    print("Maaf, file anda tidak ditemukan")
    print('Perhatikan alamat file tersebut, lalu silakan masukkan kembali')
