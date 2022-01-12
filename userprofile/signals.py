from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        user = instance
        profile = UserProfile.objects.create(
            user = user, 
            username = user.username,
            email = user.email, 
            name = user.first_name,
        )


@receiver(post_save, sender=UserProfile)
def update_profile(sender, instance, created, **kwargs):
    print(instance)
    profile = instance
    print(profile.email)
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username 
        user.save()

    # Issue----- #email or first_name parameter cannot be null 
        