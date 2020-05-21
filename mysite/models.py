from django.db import models


class Contact(models.Model):
    email     =   models.CharField(max_length=30)
    subject   =   models.CharField(max_length=100)
    message   =   models.TextField(max_length=300)

    def __str__(self):
        return self.email
    