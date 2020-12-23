import requests

class Github:
    def __init__(self):
        self.api_url='http://api.github.com'
        self.token='2a0cebe35888589a756953098fb345a5c26fc79b#'  #sadikturan  token
    def getUser(self,username):
        response=requests.get(self.api_url+'/users/'+username)
        return response.json()  ##bunu json modülünü import edip json.loads(response) şeklindede yapabiliriz.

    def getRepository(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createReposity(self,name):
        response=requests.post(self.api_url+'/users/repos?access_token='+self.token,json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True})
           
        return response


github=Github()


while True:
    secim=input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçiminiz: ")
    if secim=='4':
        break
    elif secim=='1':
        username=input('username giriniz: ')
        result=github.getUser(username)
        print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")

    elif secim=='2':
        username=input('username giriniz: ')
        result=github.getRepository(username)
        for repo in result:
           print(repo['name'])
    elif secim=='3':
        name=input('name giriniz: ')
        result=github.createReposity(name)
        print(result)
    else:
        print('yanlış seçim yaptınız.')