from django.shortcuts import render
from .models import Booking

# Create your views here.
def index(request):

    book1 = Booking()
    book1.name = "e.g Freddie"
    book1.phone = "e.g 347-887-4740"
    return render(request, "index.html", {"book1":book1})

    
