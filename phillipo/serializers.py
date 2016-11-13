from rest_framework import serializers
from phillipo.models import Member, Contact

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ('id','photo','name', 'gender','home_address','work_address',
		          'cell_phonenumber','website','previous_church',
				  'memberNumber','employed','pensioner','membership_status',
				  'special_ministries','place_of_birth','birth_month',
				  'birth_day','birth_year','marital_status', 'contact',
				  'number_of_children','highest_level_of_education','profession',
				  'classNumber','qualification','skills','hobbies',
				  'date_of_baptism','date_of_conversion','church_of_baptism',
				  'baptised_by','date_of_phillippo_membership','clubs',
				  'church_activity','additional_remarks')

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('id', 'contact_name', 'contact_relationship', 'contact_home_address',
		'contact_work_address', 'contact_email_address', 'contact_cell_phonenumber',
		'contact_home_phonenumber', 'contact_work_phonenumber', 'contact_church')
