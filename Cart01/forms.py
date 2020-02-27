from django import forms

#class UserForm(forms.ModelForm):
#    class Meta:
#        model = signUp
#        widgets = {
#            'password': forms.PasswordInput()
#        }

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)