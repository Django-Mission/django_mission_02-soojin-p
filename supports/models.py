from tkinter.messagebox import QUESTION
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

#질문 모델
class Faq(models.Model):
    CHOICES =(
        (0,'일반'),
        (1,'계정'),
        (2,'기타'),
        )

    category = models.CharField(max_length=2,choices=CHOICES,default=0)
    question = models.TextField(verbose_name='질문')
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    answer = models.TextField(verbose_name='답변')
    modifier = models.CharField(max_length=20,unique=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add =True)
    modified_date = models.DateTimeField(auto_now=True)

#답변 모델
# class Ans(models.Model):
#     answer = models.TextField(verbose_name='답변')
#     #modifier = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
#     modifier = models.CharField(max_length=20,unique=True)
#     created_at = models.DateTimeField(verbose_name='작성일', auto_now_add =True)
#     modified_date = models.DateTimeField(auto_now=True)