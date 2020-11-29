#membuka file
try :
    namaFile = input ("Silakan masukkan nama file yang ingin anda cari : ")
    bukaFile = open (namaFile, "r")
    kondisi = True
    bukaFile = open(namaFile, "a")
    
#menambahkan isi file   
    while (kondisi == True):
        isi_file = input ("silakan masukkan data yang ingin anda tambahkan :")
        bukaFile.write(isi_file)
        bukaFile.write("\n")
        
        konfirmasi = input ("Apakah Anda mau lagi? (y/n) :")
        if (konfirmasi != 'y'):
            kondisi = False
            bukaFile = open (namaFile, "r")
            print ("berikut tampilan dari file tersebut \n")
            print(bukaFile.read())
            bukaFile.close()
            
#jika Akses ditolak, maka munculkan exception ini
except (PermissionError):
    print ("Silakan periksa kembali nama file yang ingin anda cari")
    
#jika file tidak ditemukan, maka munculkan exception ini
except (FileNotFoundError):
    print ("Maaf, file anda tidak ditemukan")
    print ("Silakan periksa kembali alamat file anda")
