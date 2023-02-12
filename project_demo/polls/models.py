from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DataTimeField('date published')

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_test = models.CharField(max_length=200)
    votes = models.IntegerFeild(default=0)