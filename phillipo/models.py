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
    photo = models.ImageField(upload_to='images/', max_length=255)

    name = models.CharField(max_length=255, default='000')
    address = models.CharField(max_length=255, default='000')

    birth_month = models.CharField(max_length=255, default='000', choices=MONTHS)
    birth_day = models.CharField(max_length=255, default='000', choices=[(str(x), str(x)) for x in range(1, 32)])
    birth_year = models.CharField(max_length=255, default='000')

    profession = models.CharField(max_length=255, default='000')
    ministry = models.CharField(max_length=255, default='000')
    classNumber = models.CharField(max_length=255, default='000')

    def __str__(self):
        return self.name
