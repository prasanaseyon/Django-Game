from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


def upload_to(instance, filename):
    return 'images/{}/{}'.format(instance.pk, filename)


class Post(models.Model):
    id = models.AutoField(primary_key=True)  # Add the AutoField for the ID field
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    image_url = models.URLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})
