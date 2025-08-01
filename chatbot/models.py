from django.db import models

class Chat(models.Model):
  prompt = models.CharField(max_length = 255)

class Answer(models.Model):
  # answer = 

class User(models.Model):
  username = models.CharField(max_length=30)

class Account(models.Model):
  username = User.username
  password = models.CharField(max_length=30)
