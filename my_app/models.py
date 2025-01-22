from django.db import models
# import the built-in User model that you want to extend.
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # a OneToOneField object called user, representing the profile’s connection to the user. profile gets deleted if user does.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #  a ManyToManyField object with the field name follows, which can hold connections to other user profiles.
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
