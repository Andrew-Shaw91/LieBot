from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Chat(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='saved_chats')
    prompt = models.TextField()
    answer = models.TextField()