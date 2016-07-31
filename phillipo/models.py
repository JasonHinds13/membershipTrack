from django.db import models

MONTHS = (
        ('Jan','January'),
        ('Feb','February'),
        ('Mar','March'),
        ('Apr','April'),
        ('May','May'),
        ('Jun','June'),
        ('Jul','July'),
        ('Aug','August'),
        ('Sep','September'),
        ('Oct','October'),
        ('Nov','November'),
        ('Dec','December'),
)

# Create your models here.

class Member(models.Model):
    photo = models.ImageField(upload_to='images/')

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    birth_month = models.CharField(max_length=9, choices=MONTHS)
    birth_day = models.CharField(max_length=31, choices=[(str(x), str(x)) for x in range(1, 32)])
    birth_year = models.CharField(max_length=255)

    profession = models.CharField(max_length=255)
    ministry = models.CharField(max_length=255)
    classNumber = models.CharField(max_length=255)

    def __str__(self):
        return self.name
