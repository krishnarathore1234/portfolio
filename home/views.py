from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"


# def index(request):
#     return render(request, 'index.html')