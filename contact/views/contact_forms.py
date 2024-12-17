from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from contact.forms import ContactForm

from contact.models import Contact

def create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)

        return render(
            request,
            'contact/create.html',
            {
                'form': form
            }
        )
    
    form = ContactForm()
    
    return render(
        request,
        'contact/create.html',
        {
            'form': form
        }
    )


