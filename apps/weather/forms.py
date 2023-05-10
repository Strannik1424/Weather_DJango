from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control mt-3 mb-3',
                'id':'city',
                'name':'city',
                'type':'text',
                'placeholder':'Введите город'
            })
        }