from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'contact/index.html',
        {
            'title': 'Contact',
            'message': 'Message from the contact page.',
        }
    )
