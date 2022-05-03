from django.urls import path
from .views import contact,PostView, postcreate

urlpatterns = [
    path('contact/', contact, name = 'contact'),
     path('post/', PostView, name = 'posts'),
     path('create/', postcreate , name = 'create'),
]
