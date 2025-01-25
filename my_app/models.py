from django.db import models
# import the built-in User model that you want to extend.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    # a OneToOneField object called user, representing the profile’s connection to the user. profile gets deleted if user does.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
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
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]  # Return the first 20 characters of the content

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


