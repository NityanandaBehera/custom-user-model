from django.db import models
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
TAGS=(('TECH','TECH'),('JOBS','JOBS'),('DJANGO','DJANGO'),('REACT','REACT'))

class Category(models.Model):
    Category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Category_name


class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    tags=models.CharField(choices=TAGS,max_length=100,default='TECH')
    content=RichTextField()
    extra_title=models.CharField(max_length=100,blank=True,null=True)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title
