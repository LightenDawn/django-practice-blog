from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def starting_pages(request):
    return render(request, "blog/index.html")

def posts(request):
    pass

def post_datail(request):
    pass