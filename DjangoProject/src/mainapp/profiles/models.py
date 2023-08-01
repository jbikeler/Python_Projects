from django.db import models

# Create your models here.
TYPE_PREFIX = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
}

class Profile(models.Model):
    prefix = models.CharField(max_length=60, default="", choices=TYPE_PREFIX)
    first_name = models.CharField(max_length=60,default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.name