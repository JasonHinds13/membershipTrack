from rest_framework import serializers
from phillipo.models import Member

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ('id','photo','name','address',
                'birth_month','birth_day','birth_year',
                'profession','ministry','classNumber')
