from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail

from .models import About
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        send_mail(form.data["name"], form.data["message"], form.data["email"], ['lufitorony@gmail.com'],
                  fail_silently=False)
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = '_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["about"] = About.objects.all()
        return context
