from django.shortcuts import render
<<<<<<< HEAD
from .models import Contact

# Create your views here.
def contact(request):
    contacts = {
        'contacts':Contact.objects.all()
    }
    return render(request, 'contact/contact.html', contacts)
=======

# Create your views here.
def contact(request):
    return render(request, "contact/contact.html")
>>>>>>> 7aa53a6dd013dc37f354cf930508aa4e74b902c0
