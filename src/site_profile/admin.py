from django.contrib import admin
from site_profile.models import (
                                        About, 
                                        TermsAndCondition,
                                        Copyright,
                                        )
# Register your models here.
admin.site.register(About)
admin.site.register(TermsAndCondition)
admin.site.register(Copyright)

