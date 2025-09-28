import datetime
from django.db import models
from django.utils import timezone

class Questions(models.Model):  # Singular
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)  # Singular
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
