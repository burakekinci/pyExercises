"""
Burak Ekinci  - python
"""
from os import system

#ui
def printUI():
    print("-------------------------")
    print('1-Öğrenci Kaydet\n2-Öğrencileri Listele\n3-Ders Ekle\n'
        '4-Dersleri Listele\n5-Not Ekle\n6-Notları Listele\n7-Çıkış')
    print("-------------------------")

#öğrenci ekle seçeneği
def addStudent():
       #eklenmek istenen öğrenci sayısı için döngü
        numOfStd = numberOfObjCheck('Eklemek istediğiniz öğrenci sayısını giriniz: ')
        for i in range(1,numOfStd+1):
            isOkay=False
            while isOkay ==False:
                try:
                   id = int(input(f"{i}.öğrencinin numarası : "))
                   if(Student.search(id)==True):                            #bu öğrenci id sinde biri varsa
                       print("bu öğrenci numarasına sahip biri zaten var")
                       continue
                   assert id>0
                   fname = input(f"{i}.öğrencinin adı : ")
                   lname = input(f"{i}.öğrencinin soyadı : ")
                   isOkay=True
                except AssertionError:                                      #uygun olmayan int girilirse
                    print("öğrenci no negatif olamaz")
                    continue
                except ValueError:                                          #int girilmezse
                    print("lütfen uygun sayı veya kelime giriniz")
                    continue
            print("\n")
            Student.add(id,fname,lname)                                     #student sınıfından obje ekle

#öğrencileri yazdır seçeneği
def displayStdList():
    for i in range (studentList.__len__()):     #student objelerinden oluşan studentListin bütün elemanlarını display et
        Student.display(studentList[i])

#ders ekle seçeneği
def addLecture():
    #eklenmek istenen sayı kadar ders için döngü
    numOfLec = numberOfObjCheck('Eklemek istediğiniz ders sayısını giriniz: ')
    for i in range(1,numOfLec+1):
        isOkay = False
        while isOkay==False:
            try:
                id = int(input(f"{i}.dersin numarası : "))
                if(Lecture.search(id)==True):                               #bu ders id sinde ders varsa
                    print("bu ders numarasına sahip ders zaten var")
                    continue
                assert id>0
                name = input(f"{i}.dersin adı : ")
                isOkay=True
            except AssertionError:                                          #uygun olmayan int girilirse
                print("ders no negatif olamaz")
                continue
            except ValueError:                                              #int girilmezse
                print("lütfen uygun sayı veya kelime giriniz")  
                continue
        print("\n")
        Lecture.add(id,name)                                                #lecture sınıfından obje ekle

#dersleri yazdır seçeneği
def displayLecList():
    for i in range(lectureList.__len__()):      #lecture objelerinden oluşan lectureListin bütün elemanlarını display et
        Lecture.display(lectureList[i])

#not ekle seçeneği
def addGrade():
    #eklenmek istenen sayı kadar not için döngü
    numOfGrade = numberOfObjCheck('Eklemek istediğiniz not sayısını giriniz: ')
    for i in range(1,numOfGrade+1):
        isOkay=False
        while isOkay==False:
            try:
                std_id = int(input(f"{i}.not için öğrencinin numarası : "))
                assert std_id>0
                lect_id = int(input(f"{i}.not için dersin numarası : "))
                assert lect_id>0
                score = int(input(f"{i}.not için değer : "))
                assert score>=0 and score<=100
                isOkay=True
            except AssertionError:                                          #uygun olmayan int girilirse
                print("Uygun değerler giriniz") 
                continue
            except ValueError:                                              #int girilmezse
                print("lütfen sayı giriniz")
                continue
            if(Grade.search(std_id,lect_id)==False and isOkay==True):       #belirtilen öğrenci veya ders yok ise
                print("bu öğrenci veya ders mevcut değildir")
                isOkay =False
                continue
        Grade.add(std_id,lect_id,score)                                     #grade sınıfından obje ekle

#notları yazdır seçeneği
def displayGradeList():
    for i in range(gradeList.__len__()):        #grade objelerinden oluşan gradeListin bütün elemanlarını display et
        Grade.display(gradeList[i])        

#çıkış seçeneği
def option7():
    exit(0)    

#eklenmek istenen obje için belirtilen ekleme sayısının uygunluğunu kontrol eden fonksiyon
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

#öğrenci sınıfı
class student:
    #constructor
    def __init__(self,id,fname,lname):
        self.id = id
        self.fname = fname 
        self.lname = lname

    #öğrenci ekleme
    def add(self,Id,Fname, Lname):
        ob = student(Id,Fname,Lname)            #girilen parametrelere göre student objesi oluştur
        studentList.append(ob)                  #oluşturulan student objesini studentList içine ekle

    #öğrenci arama
    def search(self,id):                        #girilen parametre id sinde bir öğrenci studentList içinde varsa true döndür
        for i in range(studentList.__len__()):
            if(studentList[i].id == id):
                return True

    #öğrenci gösterme
    def display(self,ob):
        print("....................")
        print("No      : ",ob.id)
        print("İsim    : ",ob.fname)
        print("Soyisim : ",ob.lname)
        
#ders sınıfı
class lecture:
    #constructor
    def __init__(self,id,name):
        self.id = id
        self.name = name

    #ders ekleme
    def add(self,Id,Name):
        ob = lecture(Id,Name)                   #girilen parametrelere göre lecture objesi oluştur
        lectureList.append(ob)                  #oluşturulan lecture objesini lectureList içine ekle

    #ders arama
    def search(self,id):                        #girilien parametre id sinde bir ders lectureList içinde varsa true döndür
        for i in range(lectureList.__len__()):
            if(lectureList[i].id==id):
                return True

    #dersleri göster
    def display(self,ob):
        print("....................")
        print("Ders No : ",ob.id)
        print("Ders    : ",ob.name)                    

#not sınıfı
class grade:
    #constructor
    def __init__(self,std_id,lect_id,score):
        self.std_id = std_id
        self.lect_id = lect_id
        self.score = score

    #not ekle
    def add(self,stdId,lectId,Score):
        ob = grade(stdId,lectId,Score)          #girilen parametrelere göre grade objesi oluştur
        gradeList.append(ob)                    #oluşturulan grade objesini gradeList içine ekle
    
    #not ara
    def search(self,std_id,lect_id):            #girilen parametre id lerinde bir öğrenci ve ders varsa true döndür ve döngüden çık
        isExists = False
        for i in range(studentList.__len__()):
            for j in range(lectureList.__len__()):
                if(std_id == studentList[i].id and lect_id == lectureList[j].id):
                    isExists = True
                    break
            if(isExists==True):
                break
            else:
                isExists = False
        return isExists

    #not göster
    def display(self,ob):
        for i in range(studentList.__len__()):
            if(ob.std_id == studentList[i].id): #grade objesindeki std_id ile studentListteki id eşitse o id deki student objesinin ismini ve soyismini al
                _stdName = studentList[i].fname
                _stdLname = studentList[i].lname
        for i in range(lectureList.__len__()):  #grade objesindeki lect_id ile lectureListteki id eşitse o id deki lecture objesinin ismini al
            if(ob.lect_id == lectureList[i].id):
                _lectName = lectureList[i].name        
        for i in range(gradeList.__len__()):    #grade objesindeki score ile gradeListteki score eşitse o score'u al
            if(ob.score == gradeList[i].score):
                _score = gradeList[i].score    

        print("-------------------------------------------------")
        print("%-15s %-15s %-15s %s" %("AD","SOYAD","DERS","NOT"))
        print("%-15s %-15s %-15s %d " %(_stdName,_stdLname,_lectName,_score))
        print("\n")


#switch-case tanımlaması
def switch(choose):    
    try:
        case={
            1: addStudent,
            2: displayStdList,
            3: addLecture,
            4: displayLecList,
            5: addGrade,
            6: displayGradeList,
            7: option7,
            'default': lambda : print("yanlış değer")
        }
        return case[choose]()
    except KeyError:
        return case['default']()    
   
studentList = []
lectureList = []
gradeList = []

Student = student(0,'','')
Lecture = lecture(0,'')
Grade = grade(0,0,'')

#konsolun temizlenip yeniden seçim yapmasının istenmesi
while True:
    system("cls")
    printUI()
    try:
        choose=int(input("Seçiminizi giriniz : "))
        switch(choose)
    except ValueError:
        print("Girdiğiniz değer bir sayı değil")    
    input("devam etmek için bir tuşa basın...")
       
    
    






