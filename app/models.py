import django.contrib.auth.models
from django.db import models


class Profile (models.Model):
    name = models.CharField(max_length=255)
    birth_day = models.DateField()
    user = models.OneToOneField(django.contrib.auth.models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question (models.Model):
    tittle = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    who_asked = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle


class Answer (models.Model):
    tittle = models.CharField(max_length=255)
    text = models.TextField()
    correct = models.BooleanField()
    who_answer = models.OneToOneField(Profile, on_delete=models.CASCADE)
    what_question = models.OneToOneField(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle


class Like (models.Model):
    what_question = models.OneToOneField(Question, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.what_question
