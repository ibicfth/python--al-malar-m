from django.db import models

# Create your models here.

## model oluşturalım tabi bu modeller database de tablo olacak
##modellerin parametre olarak models.model den türemelidir.

class Movie(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=True)
    ## istersek bu tanımlara 2.parametre olarak verbose_name='' deyip;
    ## tanımlara isimle atayabiliriz örneğin name tanımına
    ##verbose_name='film adı: ' diyebiliriz.
    
    ##yukarıda eklediğimiz her yeni kolon dan sonra migrate eklememiz lazım

    def __str__(self): ##movie klası çağrıldığında hangi özelliğinin gelmesini istiyorsak;
        return self.name

    
    def get_image_path(self):
        return '/img/' + self.image

