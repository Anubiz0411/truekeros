#!usr/local/bin
# coding: latin-1

from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactUsuarioAnonimoForm, ContactUsuarioLoginForm
from django.views import generic

class ContactView(generic.FormView):

    template_name = 'home/contact.html'
    success_url = reverse_lazy('home.contact')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.form_class = ContactUsuarioLoginForm
        else:
            self.form_class = ContactUsuarioAnonimoForm
        return super(ContactView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        subject = form.cleaned_data.get('subject')
        body = form.cleaned_data.get('body')
        if self.request.user.is_authenticated():
            email_usuario = self.request.user.email
            send_email_contact(email_usuario, subject, body)
        else:
            email_usuario = form.cleaned_data.get('email')
            send_email_contact(email_usuario, subject, body)
        messages.success(self.request, 'Email enviado con exito')
        return super(ContactView, self).form_valid(form)

