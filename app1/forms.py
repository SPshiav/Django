from django import forms
from app1.models import train_details
class train_form(forms.ModelForm):
    class Meta:
        model = train_details
        fields = '__all__'
    # train_num = forms.IntegerField()
    # train_name= forms.CharField()
    # origin_city= forms.CharField()
    # destination_city= forms.CharField()
    # departure_time= forms.TimeField()
    # arrivaal_time= forms.TimeField()