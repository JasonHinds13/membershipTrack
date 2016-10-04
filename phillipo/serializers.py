from rest_framework import serializers
from phillipo.models import Member

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ('id','photo','name', 'gender','home_address','work_address',
		          'cell_phonenumber','website','previous_church',
				  'place_of_birth','birth_month','birth_day','birth_year',
				  'marital_status', 'number_of_children',
				  'highest_level_of_education','profession','ministry',
				  'classNumber','qualification','skills','hobbies',
				  'date_of_baptism','date_of_conversion','church_of_baptism',
				  'baptised_by','date_of_phillippo_membership','clubs',
				  'church_activity','additional_remarks')
