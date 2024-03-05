from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_user(AbstractUser):
    USER =[
        ('reader','Reader'),
        ('writter','Writter')
    ]
    
    city=models.CharField(max_length=100,null=True)
    user_type=models.CharField(choices=USER,max_length=100)

class BlogModel(models.Model):
    blog_title=models.CharField(max_length = 100, null=True)
    blog_describtion=models.TextField(max_length = 300, null=True)
    Image=models.ImageField(upload_to="media/blog_pic",null=True)
   
class writterProfile(models.Model):
    user = models.OneToOneField(Custom_user,null=True, on_delete = models.CASCADE, related_name='reader')
    Name=models.CharField(max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    number=models.CharField(max_length=100,null=True)
    Image=models.ImageField(upload_to="media/profile_pic",null=True)
    recent_blog= models.ForeignKey(BlogModel,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class ReaderProfile(models.Model):
    user = models.OneToOneField(Custom_user,null=True, on_delete = models.CASCADE, related_name='writter')
    Name=models.CharField(max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    number=models.CharField(max_length=100,null=True)
    Image=models.ImageField(upload_to="media/profile_pic",null=True)
    recent_blog= models.ForeignKey(BlogModel,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

   
