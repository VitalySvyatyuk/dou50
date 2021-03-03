from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

