from django import forms
from.models import Students


class studentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_number','first_name','last_name','email','course','Grade']
        labels={
            'student_number':'id',
            'first_name':'first name',
            'last_name':'Last name',
            'email':'email',
            'course':'course taken',
            'Grade':'Grade achieved'
        }

        widgets = {
          'student_number':forms.NumberInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'Grade':forms.TextInput(attrs={'class':'form-control'})



        }