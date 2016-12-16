
from django import forms


# our new form
class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['subject'].label = "Subject"
            self.fields['email'].label = "Your email:"
            self.fields['message'].label = "Your message"

