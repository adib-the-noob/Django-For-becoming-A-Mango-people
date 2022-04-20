from django.urls import path
from .views import contact,PostView

urlpatterns = [
    path('contact/', contact, name = 'contact'),
     path('post/', PostView, name = 'posts'),
]
