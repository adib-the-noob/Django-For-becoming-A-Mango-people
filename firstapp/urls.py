from django.urls import path
from .views import contact,PostView, postcreate,ContactView

urlpatterns = [
     path('contact/', ContactView.as_view(), name='contact'),
     #path('contact/', contact, name = 'contact'),
     path('post/', PostView, name = 'posts'),
     path('create/', postcreate , name = 'create'),
]
