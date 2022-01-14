from django.forms import ModelForm, models
from .models import Post


class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['profile', 'title', 'description', 'tags']