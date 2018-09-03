from django.db import models
from django.utils import timezone

class Post(models.Model): #Post es el nombre de nuestro (modelo, models.Model) significa que Post es un modelo de Django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #texto limitado
    text = models.TextField() #texto sin límite
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #método publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #método que devuelve
        return self.title