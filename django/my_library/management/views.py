from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import render,redirect

# Create your views here.

from .models import reader

def home(request):
    return render(request,'home.html',context={"current_tab":"home"})


def readers(request):
    return render(request,'readers.html',context={"current_tab":"readers"})


def books(request):
    return render(request,'books.html',context={"current_tab":"books"})

def mybag(request):
    return render(request,'mybag.html',context={"current_tab":"mybag"})

def returns(request):
    return render(request,'returns.html',context={"current_tab":"returns"})


def save_student(request):
    student_name = request.POST['student_name']
    return render(request,'welcome.html',context={'student_name' : student_name})


def readers_tab(request):
    readers = reader.objects.all()
    return render(request,'readers.html',context={'current_tab': 'readers','readers':readers})


def save_reader(request):
    reader_item = reader(reference_id = request.POST['reader_ref_id'],
                         reader_name = request.POST['reader_name'],
                         reader_contact = request.POST['reader_contact'],
                         reader_address = request.POST['reader_address'],
                         active=True)
    

    reader_item.save()
    return redirect('/readers')