from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile
from .models import UserProfile

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(customUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})



class updateUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'username', 'short_intro', 'bio', 'country', 'social_github', 'social_website', 'social_instagram', 'social_twitter']

        labels = {
            'social_github': 'Github',
            'social_website':'Website',
            'social_instagram': 'Instagram', 
            'social_twitter': 'Twitter',
        }


    def __init__(self, *args, **kwargs):
        super(updateUserProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})
