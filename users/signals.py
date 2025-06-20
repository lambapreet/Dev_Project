from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# @receiver(post_save, sender=Profile)   
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        
def deleteuser(sender, instance, **kwargs):
    print('Delete user')
    
post_save.connect(createProfile,sender=User)
post_save.connect(updateUser, sender=Profile)
post_save.connect(deleteuser,sender=Profile)