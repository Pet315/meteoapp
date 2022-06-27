from django.db import models


class Actor(models.Model):
    image = models.ImageField("Image", upload_to='images/')
