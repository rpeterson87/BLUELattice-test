from django.shortcuts import render
from django.views import View # this is the view class to handle requests
from django.http import HttpResponse # This is a class to handle sending a type of response for testing routes



# Create your views here.

class Home(View):
    def get(self, request):
        #return response for testing. 
        return HttpResponse("Bluelattice Home")