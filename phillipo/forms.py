from django import forms
from .models import Contact
from .models import Member

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['contact']
