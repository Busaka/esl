from django.shortcuts import render
from site_profile.models import (
                                        About, 
                                        TermsAndCondition,
                                        Copyright,
                                        )

# Create your views here.
def about(request):
    about = About.objects.all()
    return render(request, 'site_profile/about.html', {'about': about})

def terms_conditions(request):
    terms_conditions = TermsAndCondition.objects.all()
    return render(request, 'site_profile/terms_and_conditions.html',
            {'terms_conditions': terms_conditions })

def copyright(request):
    copyright = Copyright.objects.all()
    return render(request, 'site_profile/copyright.html',
            {'copyright': copyright })
