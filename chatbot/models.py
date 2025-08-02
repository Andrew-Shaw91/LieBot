from django.db import models

class Chat(models.Model):
  prompt = models.CharField(max_length = 255)
  answer = models.CharField(max_length = 255)

class Account(models.Model):
  username = models.CharField(max_length = 30)
  password = models.CharField(max_length = 30)
  savedChats = models.ForeignKey(Chat, on_delete = models.CASCADE)
