"""
Burak Ekinci - python
"""

#Not ortalaması hesaplayan program
print("---------------------------------------")
print("---NOT ORTALAMASI HESAPLAYAN PROGRAM---")
print("#######################################")
isim = input("isminizi giriniz : ")

#girilen input bir sayı mı testi
while True:
    vize = input("vize puanını giriniz : ")
    if vize.isdigit():
        vize = int(vize)
        if vize<0 or vize >100:
            continue
        else:
            break
    
#girilen input bir sayı mı testi    
while True:    
    final = input("final puanını giriniz : ")
    if final.isdigit():
        final = int(final)
        if final <0 or final >100:
            continue   
        else:
            break 
    
    
sonuc = float((vize + final) /2)
if(sonuc>=90 and sonuc<=100):
    harf = "AA"
elif(sonuc>=85 and sonuc<90):
    harf ="BA"
elif (sonuc>=80 and sonuc<85):
    harf = "BB"
elif (sonuc>=75 and sonuc<80):
    harf = "CB"
elif (sonuc>=70 and sonuc<75):
    harf = "CC"
elif (sonuc>=65 and sonuc<70):
    harf = "DC"
elif (sonuc>=60 and sonuc<65):
    harf = "DD"
elif (sonuc>=50 and sonuc<60):
    harf = "FD"
elif (sonuc>= 0 and sonuc<50):
    harf = "FF"

print(isim,sonuc,harf)

"""
-------------------------------------------------

"""

#Mükemmel sayı tespit eden program
print("---------------------------------------")
print("---MÜKEMMEL SAYI TESPİT EDEN PROGRAM---")
print("#######################################")

#girilen input bir sayı mı testi
while True:
    sayi = input("sayı giriniz : ")
    if sayi.isdigit():
        sayi = int(sayi)
        break   

#input mükemmel sayı mı testi
toplam = 0
for i in range(1,sayi):
    if(sayi%i==0):
        toplam+=i

if(sayi==toplam):
    print(sayi,"bir mükemmel sayıdır")
else:
    print(sayi, "bir mükemmel sayı DEĞİLDİR!")            

"""
-------------------------------------------------

"""

#Klavyeden girilen kelimenin uzunluğunu faktöriyel olarak hesaplayan program
print("---------------------------------------")
print("---KELİME UZUNLUĞUNA GÖRE FAKTÖRİYEL---")
print("#######################################")

kelime = str(input("bir kelime giriniz : "))
sonuc = 1
fac = len(kelime)

for i in range(fac,1,-1):
    sonuc *= i
 
print(sonuc)

"""
-------------------------------------------------

"""

#Asallık testi
print("-------------------------------------")
print("---ASAL SAYIYI TESPİT EDEN PROGRAM---")
print("#####################################")

#girilen input sayı mı testi
while True:
    sayi = input("sayı giriniz : ")
    if(sayi.isdigit()):
        sayi = int(sayi)
        break

for i in range(2,int(sayi/2)+1):
    if(sayi%i==0):
        print(sayi,"bir asal sayı değildir")
        break
    else:
        print(sayi,"bir asal sayıdır")  
        break  



"""
-------------------------------------------------

"""

#Asal çarpan
print("-----------------------------------------")
print("---ASAL ÇARPANLARI TESPİT EDEN PROGRAM---")
print("#########################################")

#girilen input sayı mı testi
while True:
    sayi = input("sayı giriniz : ")
    if(sayi.isdigit()):
        sayi = int(sayi)
        break

carpanlar = []
for i in range(2,int(sayi/2)+1):
    if(sayi%i==0):
        carpanlar.append(i)

print(carpanlar)