from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

def index(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'contact/index.html',
        {
            'page_obj': page_obj
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
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'contact/index.html',
        {
            'page_obj': page_obj
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
