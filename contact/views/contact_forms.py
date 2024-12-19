from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm

from contact.models import Contact

def create(request: HttpRequest) -> HttpResponse:
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/create.html',
            {
                'form': form,
                'form_action': form_action,
            }
        )
    
    form = ContactForm()
    
    return render(
        request,
        'contact/create.html',
        {
            'form': form,
            'form_action': form_action,
        }
    )

def update(request: HttpRequest, contact_id: int) -> HttpResponse:
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True
    )

    form_action = reverse('contact:update', args=(contact_id,))
    print(form_action)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact, files=request.FILES)

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/create.html',
            {
                'form': form,
                'form_action': form_action,
            }
        )
    
    form = ContactForm(instance=contact)
    
    return render(
        request,
        'contact/create.html',
        {
            'form': form,
            'form_action': form_action,
        }
    )

def delete(request: HttpRequest, contact_id: int) -> HttpResponse:
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
    )

    # contact.delete()
    # return redirect('contact:index')
    confirmation = request.POST.get('confirmation', '0')

    print(confirmation)

    if confirmation == '1':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact_single.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
