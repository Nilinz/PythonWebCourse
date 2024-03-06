from django import forms
from .models import Quote, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    tags = forms.CharField(max_length=255, label='Tags', required=True, help_text='Enter tags separated by commas')
    author = forms.CharField(max_length=255, label='Author', required=True)

    class Meta:
        model = Quote
        fields = ['quote']
