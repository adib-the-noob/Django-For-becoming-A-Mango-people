from django.contrib import admin
from .models import Class_in, Contact,Post, Subject
# Register your models here.

#Registartion for Saving data to Database...
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Class_in)
admin.site.register(Subject)