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

def memberMonth(request, month):
    members = Member.objects.all()
    results = []

    for member in members:
        if member.birth_month == month:
            results.append(member)

    return render_to_response('members.html', {"members":results})

def search(request):
    members = Member.objects.all()
    return render_to_response('search.html', {"members":members})

def searchq(request, query):
    members = Member.objects.all()
    results = []

    if "_" in query:
        query = query.replace("_", " ")

    query = query.lower()

    for member in members:
        if (query in str(member.name).lower() or query in str(member.address).lower()
            or query in str(member.profession).lower() or query in str(member.ministry).lower()
            or query in str(member.classNumber).lower()):

            results.append(member)

    return render_to_response('search.html', {"members":results})


class ListMembers(APIView):

    def get(self,request,format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members,many=True)
        return Response(serializer.data)
