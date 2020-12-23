from dbmanager import DbManager

class App:
    def __init__(self):
        self.db=DbManager()

    def initApp(self):
        msg="*********\n1- öğrenci listesi \n2- öğrenci ekle \n3- öğrenci güncelle \n4- öğrenci sil \n5- öğretmen ekle \n6- sınıflara göre dersler \n7- çıkış (E / Ç)"

        while True:
            print(msg)
            islem=input("işlem seçiniz: ")
            if islem=='1':
                self.displayStudents()
            elif islem=='2':
                pass

            elif islem=='3':
                pass

            elif islem=='4':
                pass

            elif islem=='5':
                pass

            elif islem=='6':
                pass

            elif islem=='E' or islem=='Ç':
                break

            else :
                print('yanlış seçim!')


    def displayStudents(self):
        classes=self.db.getClasses()
        for i in classes:
            print(f'{i.id}:{i.name}')
        classid=int(input ('hangi sınıf: '))
        students=self.db.getStudentsByClassId(classid)
        print('öğrenci listesi')
        for index,std in enumerate(students):
            print(f'{index + 1 }--{std.name}  {std.surname}')
            


app=App()
app.initApp()