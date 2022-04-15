from django.contrib import admin
from .models import Contact,Post
# Register your models here.

#Registartion for Saving data to Database...
admin.site.register(Contact)
admin.site.register(Post)