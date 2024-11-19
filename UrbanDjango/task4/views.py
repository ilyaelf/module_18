from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request,'fourth_task/platform.html')

def products(request):
    context = {"products":['Картофель','Моркофель','Свеклофель']}
    return render(request,'fourth_task/products.html',context)

def info(request):
    return render(request,'fourth_task/info.html')