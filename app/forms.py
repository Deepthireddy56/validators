from django import forms
def check_for_n(value):
    if value[0].lower()=='n':
        raise forms.ValidationError('Name starts with n')
def check_for_len(value):
    if len(value)<=3:
        raise forms.ValidationError('Length of the characters must be greater than 3letters')
def check_for_age(value):
    if value<=18:
        raise forms.ValidationError('Age must be 18+')
    


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_n,check_for_len])
    Sage=forms.IntegerField(validators=[check_for_age])
    Sid=forms.IntegerField()
    Email=forms.EmailField(validators=[check_for_n])
