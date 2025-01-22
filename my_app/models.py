from django.db import models
# import the built-in User model that you want to extend.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    # a OneToOneField object called user, representing the profile’s connection to the user. profile gets deleted if user does.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    # a ManyToManyField object with the field name follows, which can hold connections to other user profiles.
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        # so that your users can follow someone without them following back.
        symmetrical=False,
        # users don’t need to follow anyone.
        blank=True
    )
    # returns the value of username from the associated instance of the User model
    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]

@receiver(post_save, sender=User)
# create new profile upon creating new user
# def create_profile(sender, instance, created, **kwargs):
#    if created:
#        user_profile = Profile(user=instance)
#        user_profile.save()
#        user_profile.follows.add(instance.profile)
#        user_profile.save()
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


