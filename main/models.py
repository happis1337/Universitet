from django.db import models

class Yonalish(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)


class Fan(models.Model):
    name = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=True)


class Ustoz(models.Model):
    GENDER_CHOICE = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICE)
    age = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=50, choices=(
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr')
    ))
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)


