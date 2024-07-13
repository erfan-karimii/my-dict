from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Dictionary(models.Model):
    Choices_Level = {
        'easy':'easy',
        'medium':'medium',
        'hard':'hard',
    }
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    word = models.CharField(max_length=250)
    mean = models.CharField(max_length=250)
    level = models.CharField(max_length=250,choices=Choices_Level)
    
    is_show = models.BooleanField(default=True)
    

    def __str__(self):
        return self.word


class MasoudDictionary(Dictionary):
    class Meta:
        proxy = True


class ErfanDictionary(Dictionary):
    class Meta:
        proxy = True


class Sentences(models.Model):
    text = models.TextField()
    related_word = models.ForeignKey(Dictionary,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
    
    