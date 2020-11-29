#program menghitung rerata

print ("=============================")
print ('\n')
print ('----------WELCOME------------')
print ('\n')
print ("  PROGRAM MENGHITUNG RATA-RATA  ")
print ('\n')
print ("=============================")
print ('\n')

kondisi = True
sum = 0
awal = 0

while (kondisi == True):
    try:
        bil = int (input("Silakan masukkan bilangan bulat yang anda inginkan : "))
        sum = sum + bil
        awal += 1
        
        konfirmasi = input ("Apakah anda ingin memasukkan lagi (Iyaa/Tidak) ? : ")
        if konfirmasi != 'Iyaa' :
            kondisi = False
            print('\n')
            print("Rata-rata bilangan bulat anda adalah ", sum/awal)
    except (ValueError):
        print ('Maaf, itu bukan bilangan bulat')
print('\n')
print('TERIMA KASIH') 
