from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request,'third_task/platform.html')

def products(request):
    context = {"product1":'Картофель',"product2":'Моркофель',"product3":'Свеклофель'}
    return render(request,'third_task/products.html',context)

def info(request):
    return render(request,'third_task/info.html')