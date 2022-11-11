from django.db import models

class Kofe(models.Model):
    fam = models.CharField(max_length=20)
    yosh = models.IntegerField(default=1)
    ism = models.CharField(max_length=20)


def __str__(self):
    return f"{self.fam} , {self.ism} , {self.yosh}"