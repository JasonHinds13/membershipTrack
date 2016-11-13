from django.shortcuts import render
from django.shortcuts import render_to_response, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from phillipo.models import Member, Contact
from phillipo.forms import ContactForm, MemberForm
from phillipo.serializers import MemberSerializer, ContactSerializer
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.

@login_required(login_url='/admin/login/')
def index(request):
    return render_to_response('index.html')

@login_required(login_url='/admin/login/')
def showMembers(request):
    members = Member.objects.all()
    return render_to_response('members.html', {"members":members})

@login_required(login_url='/admin/login/')
def memberMonth(request, month):
    members = Member.objects.all()
    results = []

    for member in members:
        if member.birth_month == month:
            results.append(member)

    return render_to_response('members.html', {"members":results})

@login_required(login_url='/admin/login/')
def search(request):
    members = Member.objects.all()
    return render_to_response('search.html', {"members":members})

@login_required(login_url='/admin/login/')
def searchq(request, query):
    members = Member.objects.all()
    results = []

    if "_" in query:
        query = query.replace("_", " ")

    query = query.lower()

    for member in members:
        if (query in str(member.name).lower() or query in str(member.classNumber).lower()):
            results.append(member)

    return render_to_response('search.html', {"members":results})

@csrf_exempt
@login_required(login_url='/admin/login/')
def register(request):
    memform = MemberForm(request.POST or None)
    contactform = ContactForm(request.POST or None)

    if memform.is_valid() and contactform.is_valid():
        meminstance = memform.save(commit=False)
        coninstance = contactform.save(commit=False)

        coninstance.save()
        meminstance.contact = coninstance
        meminstance.save()

    context = {'memform': memform, 'contactform': contactform}

    return render(request, 'add_member.html', context)


class ListMembers(APIView):

    def get(self,request,format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members,many=True)
        return Response(serializer.data)
