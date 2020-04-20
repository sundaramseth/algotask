from django.db import models

class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(max_length=254)
    document = models.DateTimeField('Date', blank=True, null=True)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)


    def __str__(self):
        return self.name
