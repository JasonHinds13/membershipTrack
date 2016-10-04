from django.db import models
from cloudinary.models import CloudinaryField

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

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

MARITAL_STATUS = (
    ('Single','Single'),
    ('Married','Married'),
    ('Divorced','Divorced'),
    ('Widowed','Widowed'),
)

EDUCATION = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
    ('Tertiary','Tertiary'),
)

# Create your models here.

class Member(models.Model):
    photo = CloudinaryField('pro_pic')

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER)
    classNumber = models.CharField(max_length=255)

    home_phonenumber = models.CharField(max_length=255)
    cell_phonenumber = models.CharField(max_length=255)
    work_phonenumber = models.CharField(max_length=255)

    home_address = models.CharField(max_length=255)
    work_address = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)

    website = models.CharField(max_length=255)

    previous_church = models.CharField(max_length=255)

    birth_month = models.CharField(max_length=255, choices=MONTHS)
    birth_day = models.CharField(max_length=255, choices=[(str(x), str(x)) for x in range(1, 32)])
    birth_year = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)

    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS)

    number_of_children = models.CharField(max_length=255)

    highest_level_of_education = models.CharField(max_length=255, choices=EDUCATION)

    qualification = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)

    date_of_conversion= models.CharField(max_length=255)
    date_of_baptism = models.CharField(max_length=255)
    church_of_baptism = models.CharField(max_length=255)
    baptised_by = models.CharField(max_length=255)
    date_of_phillippo_membership = models.CharField(max_length=255)

    clubs = models.CharField(max_length=255)
    church_activity = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)

    additional_remarks = models.CharField(max_length=255)

    def __str__(self):
        return self.name
