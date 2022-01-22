from django.db.models import fields
from django.forms import ModelForm, forms, models
from .models import Post, Solution
from django import forms


class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'tags']
        widgets = {
          'description': forms.Textarea(attrs={'rows':7, 'cols':15}),
        }

    def __init__(self, *args, **kwargs):
        super(postForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})


class solutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['description']
        widgets = {
          'description': forms.Textarea(attrs={'rows':5, 'cols':15}),
        }


    
    def __init__(self, *args, **kwargs):
        super(solutionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})