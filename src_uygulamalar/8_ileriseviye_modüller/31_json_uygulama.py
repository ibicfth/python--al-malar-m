import json
import os
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users=[]  ##girilen kullanıcıların bilgilerini burda listeleyip login işlemini yapmak için oluşturduk,ancak kayıt yaparken,bunu json ile çevirmemiz gerekiyor.
        self.isLoggedIn=False
        self.currentUser={}
        self.loadUsers() #load users from .json file

    def loadUsers(self):
        if os.path.exists('users.json'): #dosyanın olup olmadığını sorgular true false
            with open('users.json','r',encoding='utf-8') as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
            print(self.users)
    
    def register(self, user:User):
        self.users.append(user)
        self.savetofile()
        print('kullanıcı oluşturuldu')

    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn=True
                self.currentUser=user
                print('login yapıldı')
            break
        
    def logout(self):
            self.isLoggedIn=False
            self.currentUser={}
            print('çıkış yapıldı.')

    def identity(self):
            if self.isLoggedIn:
                print(f"username:{self.currentUser.username}")
            else:
                print('giriş yapılmadı.')

    def savetofile(self):
        list=[]  ## dosyaya yazdırılabilir liste yapmak için tanımladık, aşağıdada json moduyla bunu yazdırılabilir yaptık
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list, file)  # yazdırılabilir list'i dump ile file dosyasının içine yazdırdık.

repository = UserRepository()
while True:
    print('Menu'.center(50,'*'))
    secim=input('1- register\n2- login\n3- logout\n4- identity\n5- exit\nseçiminiz: ')
    if secim=='5':
        break
    
    elif secim=='1':
        username=input('isminizi giriniz: ')
        password=input('password giriniz: ')
        email=input('email giriniz: ')

        user=User(username=username,password=password,email=email)
        repository.register(user)

        print(repository.users)
    elif secim=='2':
        if repository.isLoggedIn:
            print('zaten giriş yaptınız.')
        else:
            username=input('username: ')
            password=input('password: ')
            repository.login(username,password)

    elif secim=='3':
        repository.logout()
    
    elif secim=='4':
        repository.identity()
    
    else:
        print('yanlış seçim')

