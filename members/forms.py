from django import forms
from .models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'description','relatedWork', 'deadline', 'appointed', 'img']
        
class WorkUpdateFormUser(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['status']

        
            
