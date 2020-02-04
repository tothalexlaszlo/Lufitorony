from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form_control", "id": "contact-name", "placeholder": "Név"}),
        max_length=200, required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form_control", "id": "contact-email", "placeholder": "Email"}),
        required=True)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form_control", "id": "contact-Subject", "placeholder": "Tárgy"}),
        max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form_control", "id": "contact-message", "placeholder": "Message"}),
        required=True)
