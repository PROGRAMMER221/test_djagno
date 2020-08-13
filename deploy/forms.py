from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['std_name','age']
        widgets = {
            'std_name' : forms.TextInput(attrs={
                'class' : 'form-control col-4'
            }),
            
            'age' : forms.NumberInput(attrs={
                'class' : 'form-control col-4'
            })
            }