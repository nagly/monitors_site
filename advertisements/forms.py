from django import forms
from advertisements.models import Buffer

class AdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.fields['weeks'] = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'weeks','min':'1', 'max': '55', 'required': '', 'class': 'form-control', 'value':'1'}),
                                                 label='Period (weeks)')
    class Meta:
        model = Buffer
        fields = ['image','url','weeks']
        widgets = {
            'url': forms.TextInput(attrs={'required': '', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'required':''}),
        }
        labels = {
        'url':'Destination URL',
        'image':'Banner',
        }