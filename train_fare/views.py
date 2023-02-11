from django.shortcuts import render
from django.http import HttpResponse
from train_fare import views
from train_fare.forms import enter_fare
# Create your views here.
def fare(Request):
    form =enter_fare()
    if Request.method=='POST':
        form = enter_fare(Request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Record Inserted Successfully</h1>")
        else:
            return HttpResponse("Error form is invailed")
    return render(Request, 'Trains_fare/fare.html', {'form':form})