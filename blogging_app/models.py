from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Contact(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(default=datetime.now)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.name