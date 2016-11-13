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

YN = (
    ('Yes','Yes'),
    ('No','No'),
)

STATUS = (
    ('Current','Current'),
    ('Inactive','Inactive'),
    ('Migrated','Migrated'),
    ('Transfered','Transfered'),
    ('Shut-in','Shut-in'),
)

ACTIVITIES = (
    ('Brotherhood','Brotherhood'),
    ("Women's Federation","Women's Federation"),
    ("Usher's Board","Usher's Board"),
    ('Youth Fellowship','Youth Fellowship'),
    ('Young Adult','Young Adult'),
    ("Decon's Board", "Decon's Board"),
)

MINISTRIES = (
    ('Audio Visual','Audio Visual'),
    ('Creative Arts','Creative Arts'),
    ('Family Life','Family Life'),
    ('Education/Continuing Education Programme','Education/Continuing Education Programme'),
    ('Harvest','Harvest'),
    ('Hospitatlity','Hospitatlity'),
    ('Mission/Evangelism','Mission/Evangelism'),
    ('Medicare, Counselling and Healing','Medicare, Counselling and Healing'),
    ('Music','Music'),
    ('Property and Building','Property and Building'),
    ('Social Outreach','Social Outreach'),
    ('Sports Ministry','Sports Ministry'),
    ('Sunday School','Sunday School'),
    ('Stewartship/Training','Stewartship/Training'),
    ('Welfare/Benevolence','Welfare/Benevolence'),
)

CONTACT = (
    ('Email', 'Email'),
    ('Text', 'Text'),
    ('Both', 'Both'),
    ('Neither', 'Neither'),
)

# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_relationship = models.CharField(max_length=255, null=True, blank=True)

    contact_home_address = models.CharField(max_length=255, null=True, blank=True)
    contact_work_address = models.CharField(max_length=255, null=True, blank=True)
    contact_email_address = models.CharField(max_length=255, null=True, blank=True)

    contact_cell_phonenumber = models.CharField(max_length=255, null=True, blank=True)
    contact_home_phonenumber = models.CharField(max_length=255, null=True, blank=True)
    contact_work_phonenumber = models.CharField(max_length=255, null=True, blank=True)

    contact_church = models.CharField(max_length=255, null=True, blank=True)

class Member(models.Model):
    photo = CloudinaryField('pro_pic', null=True, blank=True)

    name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER, null=True, blank=True)
    classNumber = models.CharField(max_length=255, null=True, blank=True)

    envelope_Number = models.CharField(max_length=255, null=True, blank=True)
    employed = models.CharField(max_length=255, choices=YN, null=True, blank=True)
    pensioner = models.CharField(max_length=255, choices=YN, null=True, blank=True)
    membership_status = models.CharField(max_length=255, choices=STATUS, null=True, blank=True)

    home_phonenumber = models.CharField(max_length=255, null=True, blank=True)
    cell_phonenumber = models.CharField(max_length=255, null=True, blank=True)
    work_phonenumber = models.CharField(max_length=255, null=True, blank=True)

    home_address = models.CharField(max_length=255, null=True, blank=True)
    work_address = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)

    website = models.CharField(max_length=255, null=True, blank=True)

    previous_church = models.CharField(max_length=255, null=True, blank=True)

    birth_month = models.CharField(max_length=255, choices=MONTHS, null=True, blank=True)
    birth_day = models.CharField(max_length=255, choices=[(str(x), str(x)) for x in range(1, 32)], null=True, blank=True)
    birth_year = models.CharField(max_length=255, null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, null=True, blank=True)

    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS, null=True, blank=True)

    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)

    number_of_children = models.CharField(max_length=255, null=True, blank=True)

    highest_level_of_education = models.CharField(max_length=255, choices=EDUCATION, null=True, blank=True)

    qualification = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)
    spiritual_gifts = models.CharField(max_length=255, null=True, blank=True)

    date_of_conversion= models.CharField(max_length=255, null=True, blank=True)
    date_of_baptism = models.CharField(max_length=255, null=True, blank=True)
    church_of_baptism = models.CharField(max_length=255, null=True, blank=True)
    baptised_by = models.CharField(max_length=255, null=True, blank=True)
    date_of_phillippo_membership = models.CharField(max_length=255, null=True, blank=True)

    clubs = models.CharField(max_length=255, null=True, blank=True)
    auxilliary = models.CharField(max_length=255, choices=ACTIVITIES, null=True, blank=True)
    special_ministries = models.CharField(max_length=255, choices=MINISTRIES, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)

    how_can_the_church_contact_you = models.CharField(max_length=255, choices=CONTACT, null=True, blank=True)

    additional_remarks = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
