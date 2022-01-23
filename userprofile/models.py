from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
import uuid



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profles/', default='profiles/default.png')
    bio = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)


    def __str__(self) -> str:
        return self.username


