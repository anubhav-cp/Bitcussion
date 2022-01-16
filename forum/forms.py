from django.db.models import fields
from django.forms import ModelForm, models
from .models import Post, Solution


class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['profile', 'title', 'description', 'tags']


class solutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['description']