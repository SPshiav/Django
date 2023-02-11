from django.shortcuts import render
from django.http import HttpResponse
from app1.models import train_details
from app1 import forms

# Create your views here.
def home(request):
    #return HttpResponse("This is my Home page")
    return render(request, "home.html")

def train_det(request):
    form=forms.train_form()
    if request.method =='POST':
        form = forms.train_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Record updated to train_details </h2>")
        else:
            return HttpResponse("Error form invaild")
    return render(request, 'Trains_fare/fare.html', {'form':form})
    #return HttpResponse("Collect train Information")

def report(request):
    train_mdl_details = train_details.objects.order_by('train_num')
    train_details_dict = {'insert_train_details': train_mdl_details}
    return render(request, 'report.html', context=train_details_dict)
   # return HttpResponse("Collect ticket Information")


