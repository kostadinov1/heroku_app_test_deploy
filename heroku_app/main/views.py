from django.shortcuts import render

# Create your views here.
from heroku_app.main.models import Note


def build_home_view(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'home.html', context)