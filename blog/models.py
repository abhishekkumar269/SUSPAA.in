from django.db import models
from django.utils.html import format_html


# Create your models here.

#categogy model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to ='category/')
    url = models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;">'.format(self.image))
    

       
    def __str__(self):
        return self.title



#category post

class Post(models.Model):
    Post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='post/')
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    url = models.CharField(max_length=100)


    
    def __str__(self):
        return self.title

    
