from django.shortcuts import render
from django.http import HttpResponse
# from portfolio.settings import EMAIL_HOST_USER

from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'mywebsite/index.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        company = request.POST['company']

        # # send an email
        # send_mail(
        #     name, # subject
        #     message, # message
        #     'contact@digait.de', # from email
        #     ['contact@digait.de'] # to email
        # )
    return HttpResponse('')
