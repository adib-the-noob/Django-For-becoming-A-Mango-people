from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from PIL import Image

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    content = models.TextField()
    
    #Model Manager
    def __str__(self):
        return self.name
class Post(models.Model):
    CATEGORY=(
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,default=title)
    email=models.EmailField()
    salary=models.FloatField()
    details=models.TextField()
    available=models.BooleanField()
    category=models.CharField(max_length=100,choices=CATEGORY)
    created_at=models.DateTimeField(default=now)
    image=models.ImageField(default='default.jpeg',upload_to='tution/images')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)