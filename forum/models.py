from django.db import models
import uuid
from django.db.models.base import Model
from django.db.models.fields import CharField
from userprofile.models import UserProfile




class Post(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=800)
    description = models.CharField(max_length=2000)
    upvote = models.IntegerField(default=0, null=True, blank=True)
    downvote = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)  
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self) -> str:
        return self.title


class Solution(models.Model):
    post = models.ForeignKey('POST', null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    upvote = models.IntegerField(default=0, null=True, blank=True)
    downvote = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description



class Tag(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.name