#soal 2
#2). buat program python dengan match case untuk menghitung luas bangun datar :
#jika pilih 1, maka menghitung luas persegi
#jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
#kalau pilihannya tidak ada maka ada keterangan : salah pilih
print('Ini adalah program sederhana untuk menghitung luas bangun datar')
print('Pilih menu angka 1-3 : \n1. persegi \n2. lingkaran \n3. segitiga')
pilih_menu =int(input('Silahkan pilih menu dengan mengetikkan angka 1-3 :'))
match pilih_menu :
    case 1 : 
        print('luas persegi')
        sisi=int(input('silahkan masukan nilai yang mau di hitung'))
        hitung = sisi*sisi
        print(f'luas persegi adalah : {hitung}')
        print('==========')   
    case 2 :
        print('luas lingkaran')
        r=int(input('silahkan masukan nilai yang mau di hitung'))
        hitung = 22/7 * r**2
        print(f'luas lingkaran adalah : {hitung}')
        print('==============')
    case 3 :
        print('luas segitiga')
        a=int(input('silahkan masukan nilai yang mau di hitung'))
        t=int(input('silahkan masukan nilai yang mau di hitung'))
        hitung = 1/2 * a * t
        print(f'luas segitiga adalah : {hitung}')
        print('==========')
    case _:    
        print ('pilihan tidak valid, silahkan pilih antara 1-3:') 
        
       
             



