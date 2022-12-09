from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('author', 'title', 'location', 'price', 'space_capacity', 'description', 'event_date', 'event_end_date')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'space_capacity': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'event_date': forms.DateTimeInput(attrs={'class':'form-control'}),
            'event_end_date': forms.DateInput(attrs={'class':'form-control'}),
        }
