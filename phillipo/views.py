import requests
from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from phillipo.models import Member
from phillipo.serializers import MemberSerializer

# Create your views here.

def index(request):
    return render_to_response('index.html')

def showMembers(request):
    members = Member.objects.all()
    return render_to_response('members.html', {"members":members})

def search(request):
    members = Member.objects.all()
    return render_to_response('search.html', {"members":members})


class ListMembers(APIView):

    def get(self,request,format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members,many=True)
        return Response(serializer.data)
