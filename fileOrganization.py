"""
Burak Ekinci  - python
"""
from os import system,name                                  #işletim sisteminin adını ve sistem fonklarını ekle
import pickle                                               #pickle modül yapısını ekle

studentData = {}                                            #öğrenci bilgilerini bulunduracak olan dictionary
lessonData = {}                                             #ders bilgilerini bulunduracak olan dictionary

#arayüzü ekrana yazdıran fonk.
def printUI():
    print("--------------------\n"
          "|1.Öğrenci Kaydet  |\n"
          "|2.Öğrenci Listele |\n"
          "|3.Ders Ekle       |\n"
          "|4.Ders Listele    |\n" 
          "|5.Çıkış           |\n"
          "--------------------")

#seçim sonrası arayüzü tazeleyen fonk.
def ClearConsole():
    if name =='nt':                                         #işletim sistemi windows ise belirtilen konsol temizleme fonkunu çağır
        _ = system("cls")
    else:                                                   #işletim sistemi macos veya linux ise belitrilen konsol temizleme fonkunu çağır
        _ = system("clear")        
    printUI()                                               #arayüzü ekrana yazdır

#seçime göre yapılacakları belirten fonk.
def ChooseOption(_choose):
    if  _choose == 1:
        saveStudent()                                       #arayüzden 1 seçilmişse öğrenci kaydet fonkunu çalıştır
    
    elif _choose == 2:
       readStudent()                                        #arayüzden 2 seçilmişse öğrenci oku fonkunu çalıştır
       displayStudent(studentData)                          #ve öğrenci bilgilerinin bulunduğu dictionary'yi öğrenci yazdır fonkuna parametre olarak ata ve çalıştır
    
    elif _choose == 3:
        saveLesson()                                        #arayüzden 3 seçilmişse öğrenci kaydet fonkunu çalıştır
    
    elif _choose == 4:
        readLesson()                                        #arayüzden 4 seçilmişse ders oku fonkunu çalıştır
        displayLesson(lessonData)                           #ve ders bilgilerinin bulunduğu dictionary'yi ders yazdır fonkuna parametre olarak ata ve çalıştır
    
    elif _choose == 5:
        exit(0)                                             #arayüzden 5 seçilmişse uygulamayı durdur ve çıkış yap
    
    else:
        print("Uygun sayı giriniz lütfen")                  #arayüzde belirtilen seçenekler dışında sayı girilmişse uyar


#eklenmek istenen obje sayısının uygunluğunu kontrol eden fonksiyon
def numberOfObjCheck(str):
    while True:
        try:
            tmp = int(input(str))
            assert tmp>=0
        except AssertionError:                                      #uygun olmayan int girilirse
            print("girmiş olduğunu sayı negatif olamaz")
            continue
        except ValueError:                                          #int girilmezse
            print("lütfen uygun sayı veya kelime giriniz")
            continue
        else:
            break
    return tmp    



#öğrencileri dosyaya kaydeden fonk.
def saveStudent():
    
    _studentData = readStudent()                        #öğrenci oku fonkundan dönen dictionary'yi local değişkene ata
    i = 1
    numOfStd = numberOfObjCheck("Eklemek istediğiniz öğrenci sayısını giriniz: ")
    while i<numOfStd+1:                                          #5 öğrenci kaydetmek için döngü
        print("\n<--------------------------------------->")
        try:
            studentId = int(input(f"{i}.Öğrencinin numarası giriniz : "))
            assert studentId>0
        except ValueError:                             #input integer değilse uyar ve döngüye o an için baştan başla
            print("\n!--Girdiğiniz değer sayı değil--!")
            continue
        except AssertionError:                         #input negatif ise uyar ve döngüye o an için baştan başla
            print("\n!--Öğrenci numarası negatif olamaz--!")
            continue
        
        if not studentId in _studentData:              #girilen id'de bir öğrenci dictionary'de yoksa öğrenci bilgilerini al dictionary'ye ekle
            studentName = input(f"{i}.Öğrencinin ismini giriniz : ")
            studentLastname = input(f"{i}.Öğrencinin soyismini giriniz : ")

            _studentData[studentId] = []               #dictionary içinde her bir öğrenci id için ayrı dizi oluştur
            _studentData[studentId].append(studentName)#her bir id için ayrı oluşturulan diziye isim ve soyisim ekle
            _studentData[studentId].append(studentLastname)
        else:                                          #girilen id'de bir öğrenci dictionary'de var ise uyar ve döngüye o an için baştan başla
            print("\n!--Bu numarada kayıtlı bir öğrenci zaten var--!")
            continue
        
        i+=1  
    
    try:
        with open('student.txt','wb') as file:          #student.txt dosyasını write binary olarak aç
            pickle.dump(_studentData,file)              #local dictionary'yi pickle modülü ile dosya içine yaz
            file.close()                                #dosyayı kapat
    except:
        print("!--Dosyaya yazmada hata oldu--!\n")      #dosyaya yazma esnasında hata olursa uyar

#öğrencileri dosyadan okuyan fonk.
def readStudent():
    f=open('student.txt','a')                              #student.txt dosyasını aç yoksa oluştur 
    f.close()                                              #dosyayı kapat
   
    try:
        with open('student.txt','rb') as file:            #student.txt dosyasını binary okumak üzere aç
            data = file.read()                            #dosyayı oku ve local data değişkenine ata
       
        global studentData                                #öğrenci bilgilerini bulunduran global dictionary'yi referans olarak al                                
        studentData = pickle.loads(data)                  #data içindeki bilgileri dictionary olarak öğrenci bilgilerini bulunduran dictionary içine at
       
        return studentData                                #öğrenci bilgilerini tutan dictionary'yi döndür
    except EOFError:                                      
        print("!--Dosya Boş--!\n")                        #dosyadan bilgi alınamadan dosya sonuna ulaşırsa dosya boş uyarısı ver  
        return studentData                                #ve boş olan ve öğrenci bilgilerini tutan dictionary'yi döndür

#öğrencileri ekrana yazdıran fonk.
def displayStudent(_dictData):
    print("___________________________________________________")
    print("%-5s %-15s %-15s %-5s %5s"%("|","No","İSİM","SOYİSİM","|"))
    print("|-------------------------------------------------|")
    for key,value in _dictData.items():
       print('{:^15s}'.format(str(key)),'{:^18s}'.format(value[0]),'{:^15s}'.format(value[1]))
    print("___________________________________________________")

#dersleri dosyaya kaydeden fonk.
def saveLesson():
    
    _lessonData = readLesson()                          #ders oku fonkundan dönen dictionary'yi local değişkene ata
    i=1
    numOfLec = numberOfObjCheck("Eklemek istediğiniz ders sayısını giriniz: ")
    while i<numOfLec+1:                                          #3 ders kaydetmek için döngü
        print("\n<--------------------------------------->")
        try:
            lessonId = int(input(f"{i}.Dersin kodunu giriniz : "))
            assert lessonId>0
        except ValueError:                              #input integer değilse uyar ve döngüye o an için baştan başla
            print("\n!--Girdiğiniz değer sayı değil--!")
            continue    
        except AssertionError:                          #input negatif ise uyar ve döngüye o an için baştan başla
            print("\n!--Ders kodu negatif olamaz--!")
            continue

        if not lessonId in _lessonData:                 #girilen id'de bir ders dictionary'de yoksa ders bilgilerini al dictionary'ye ekle
            lessonName = input(f"{i}.Dersin ismini giriniz : ")

            _lessonData[lessonId] = []                  #dictionary içinde her bir ders id için ayrı dizi oluştur
            _lessonData[lessonId].append(lessonName)    #her bir id için ayrı oluşturulan diziye ders adı ekle
        else:                                           #girilen id'de bir öğrenci dictionary'de var ise uyar ve döngüye o an için baştan başla
            print("\n!--Bu ders kodunda bir ders zaten var--!") 
            continue
        
        i+=1 
    
    try:                                                
        with open('lesson.txt','wb') as file:           #lesson.txt dosyasını write binary olarak aç
            pickle.dump(_lessonData,file)               #local dictionary'yi pickle modülü ile dosya içine yaz
            file.close()                                #dosyayı kapat
    except:
        print("!--Dosyaya yazmada hata oldu--!\n")      #dosyaya yazma esnasında hata olursa uyar

#dersleri dosyadan okuyan fonk.
def readLesson():
    f=open('lesson.txt','a')                             #lesson.txt dosyasını aç yoksa oluştur 
    f.close()                                            #dosyayı kapat
   
    try:
        with open('lesson.txt','rb') as file:            #lesson.txt dosyasını binary okumak üzere aç
            data = file.read()                           #dosyayı oku ve local data değişkenine ata
        
        global lessonData                                #ders bilgilerini bulunduran global dictionary'yi referans olarak al
        lessonData = pickle.loads(data)                  #data içindeki bilgileri dictionary olarak ders bilgilerini bulunduran dictionary içine at
        
        return lessonData                                #ders bilgilerini tutan dictionary'yi döndür
    except EOFError:
        print("!--Dosya Boş--!\n")                       #dosyadan bilgi alınamadan dosya sonuna ulaşırsa dosya boş uyarısı ver
        return lessonData                                #ve boş olan ve öğrenci bilgilerini tutan dictionary'yi döndür

#dersleri ekrana yazdıran fonk.
def displayLesson(_dictData):
    print("_______________________________________")
    print("%-5s  %-18s %-5s  %2s"%("|","Ders Kodu","Ders İsmi","|"))
    print("|-------------------------------------|")
    for key,value in _dictData.items():
        print('{:^24s}'.format(str(key)),'{:^10s}'.format(value[0]))
    print("_______________________________________")

#sürekli olarak seçimi soran döngü
while True:
    ClearConsole()                                          #konsol(arayüz) tazelenir
    try:
        choose = int(input("Lütfen seçiminizi giriniz : "))
        ChooseOption(choose)                                #inputa göre işlem yap
    except ValueError:                                      #input integer değilse uyarı ver
        print("\n!--Girdiğiniz değer sayı değil--!\n")
    input("\n---Devam etmek için bir tuşa basınız---")