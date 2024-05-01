from django.shortcuts import render
from django.http import HttpResponse

def pengguna(request):
    return HttpResponse("Selamat Datang Pengguna")
