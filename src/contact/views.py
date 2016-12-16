from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm
from .models import Contact

# Create your views here.


def contact(request):
    """TODO: Docstring for home.
    :returns: TODO
    """
    form = ContactForm(request.POST or None)
    context = {}
    if form.is_valid():

        subject = form.cleaned_data.get('subject', '')
        from_email = form.cleaned_data.get('email', '')
        message = form.cleaned_data.get('message', '')

        # send_mail(subject, message, from_email, ['info@excellencestudentmagazine.com'], fail_silently=False)
        email = EmailMessage(
                subject,
                message,
                from_email,
                ['info@excellencestudentmagazine.com'],
                headers = {'Reply-To': from_email }
            )
        email.send()
        contact = Contact.object.create(subject=subject, email=email,
                message=message)
        contact.sve()
        messages.success(request, 'Email sent successfully!')
        return HttpResponseRedirect('/')
    context.update(csrf(request))
    context.update({'form': form })
    return render(request, 'contact/contact.html', context)




