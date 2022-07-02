from http.client import HTTPResponse
from django.shortcuts import render

from travello.models import Destination
from . models import Destination
# Create your views here.
def home(request):
  
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
"""
 dest1 = Destination()
    dest1.price = 2900
    dest1.name = 'Australia'
    dest1.desc = 'Open to explore the wonderful mysteries of.....'
    dest1.img  = 'destination_1.jpg'
    dest1.offer = False
    dest2 = Destination()
    dest2.price = 900
    dest2.name = 'Peru'
    dest2.desc = 'Cools u down....'
    dest2.img  = 'destination_2.jpg'
    dest2.offer = False
    dest3  = Destination()
    dest3.name = 'San-Fransisco'
    dest3.price = 2100
    dest3.desc = 'Spend the last month here.....'
    dest3.img  = 'destination_3.jpg'
    dest3.offer = True
    dests = [dest1,dest2,dest3]""" 


