from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.contact, name="contact")
=======
    path('contact/', views.contact, name='contact')
>>>>>>> 7aa53a6dd013dc37f354cf930508aa4e74b902c0
]