from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('contact_form', views.contact_form, name='contact_form')
    url(r'^ajax/contact_form/$', views.contact_form),

]
