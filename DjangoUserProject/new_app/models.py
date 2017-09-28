from django.db import models

# Create your models here.

class User(models.Model):
    user_fn = models.CharField(max_length = 64)
    user_ln = models.CharField(max_length = 64)
    user_email = models.EmailField()

    def __str__(self):
        return self.user_fn
