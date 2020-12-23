
class Student:
    
    def __init__(self,id,studentnumber,name,surname,birthdate,gender,classid):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber=studentnumber
        if len(name)>45:
            raise Exception ("name alanına maksimum 45 karakter yollayabilirsiniz. ")
        
        self.name=name  
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
        self.classid=classid

    @staticmethod
    def CreateStudent(obj):
        liste=[]
        if isinstance(obj, tuple):
            liste.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                liste.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return liste
