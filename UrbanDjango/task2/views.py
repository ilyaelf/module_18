from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ClassView(TemplateView):
    template_name = 'class_template.html'
def func_view(request):
    return render(request,'func_template.html')


