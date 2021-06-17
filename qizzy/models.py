from django.db import models

# Create your models here.
class questions(models.Model):
    id = models.IntegerField(primary_key=True)
    ques = models.CharField(max_length=200, blank=False) 
    choi1 = models.CharField(max_length=20, blank=False)
    choi2 = models.CharField(max_length=20, blank=False)
    ans = models.CharField(max_length=20, blank=False) 
    desc = models.CharField(max_length=200, blank=False) 