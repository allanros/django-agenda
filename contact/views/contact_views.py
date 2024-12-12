from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

def index(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')

    return render(
        request,
        'contact/index.html',
        {
            'contacts': contacts
        }
    )

def search_query(request: HttpRequest) -> HttpResponse:
    search_value = request.GET.get('q', '').strip()

    if not search_value:
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

    return render(
        request,
        'contact/index.html',
        {
            'contacts': contacts
        }
    )


def contact(request: HttpRequest, contact_id: int) -> HttpResponse:
    # single_contact = Contact.objects.filter(id=contact_id).last()

    # if not single_contact:
    #     raise Http404('Contact not found')
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)

    return render(
        request,
        'contact/contact_single.html',
        {
            'contact': single_contact
        }
    )
