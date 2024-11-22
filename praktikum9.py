#1). Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0

print('## Nomor 1 ##')

def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

suhu_celcius1= 0
suhu_celcius2= 100
suhu_fahreinheit1= celcius_ke_fahrenheit(suhu_celcius1)
suhu_fahreinheit2= celcius_ke_fahrenheit(suhu_celcius2)
print('Suhu Celcius', suhu_celcius1, 'sama dengan', suhu_fahreinheit1)
print('Suhu Celcius', suhu_celcius2, 'sama dengan', suhu_fahreinheit2)

#2). Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False

print('## Nomor 2##')

def genap_ganjil(bilangan):
    hitung= bilangan % 2 == 0 #menentukan bil ganjil/genap
    return hitung #mengembalikan hitung

angka= 4
hasil= genap_ganjil(angka)
print (f"Bilangan {angka} bernilai {hasil}")

angka2= 7
hasil2= genap_ganjil(angka2)
print (f"Bilangan {angka2} bernilai {hasil2}")

#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus:
#nilai (80) #lulus
#nilai(60) #gagal

print('## Nomor 3 ##')

def nilai_ujian(nilai):
   if nilai >= 80:
       return "Lulus"
   else:
       return "Gagal"

nilai= 80
hasil= nilai_ujian(nilai)
print(f'Nilai: {nilai} adalah: {hasil}')

nilai1= 75
hasil1= nilai_ujian(nilai1)
print(f'Nilai: {nilai1} adalah: {hasil1}')

#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,19

print("## Nomor 4 ##")
def bilangan_ganjil (number):
    for a in range (1, number, 2): #1,3,5...19
        print(a, end=" ")

bilangan_ganjil(20)
    

