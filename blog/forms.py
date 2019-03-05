from django import forms
from .models import Blog


class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ['title', 'image', 'body']
        
        def __init__(self, *args, **kwargs):
            super.fields['image'].required = False
