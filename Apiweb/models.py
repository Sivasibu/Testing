from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    title =models.CharField(max_length=222)
    content =models.TextField()
    STATUS_CHOICES =(('draft','Draft'),('published','Published'))
    status =models.CharField(max_length=30,choices=STATUS_CHOICES)
    created_on =models.DateTimeField(auto_now_add=True)
    updated_on =models.DateTimeField(auto_now=True)
    
    created_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by')
    updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='updated_by')
    def __str__(self):
        return self.title