from django.shortcuts import render
import datetime
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.template.context import RequestContext


def homepage(request):
    return render(request, 'app1/index.html')

def secondpage(request):
    return render(request, 'app1/secondpage.html')

