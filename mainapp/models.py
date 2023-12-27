from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} {self.password} {self.username}"


class Client(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    descriptions_client = models.CharField(max_length=200, null=True)


class Projects(models.Model):
    name = models.CharField(max_length=200, null=True)
    descriptions_client = models.CharField(max_length=200, null=True)
    project_type = models.CharField(max_length=200, null=True)
    account_id = models.CharField(max_length=200, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class AdwData(models.Model):
    refresh_token = models.CharField(max_length=200, null=True)
    customer_id = models.CharField(max_length=200, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)


class FbData(models.Model):
    fb_client_id = models.CharField(max_length=200, null=True)
    fb_client_secret = models.CharField(max_length=200, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)