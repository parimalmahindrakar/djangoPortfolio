from django import forms
from .models import MyViews
class GetFeedback(forms.ModelForm):
    class Meta:
        model = MyViews
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
               'placeholder': 'Enter the email',
               'label':''

            }),
            'view': forms.Textarea(attrs={
                'placeholder': 'Type here ... ',
                'label':''
            })
        }

