from django.conf.urls import url
from . import views

app_name = 'ffutche'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^donation/$', views.donation, name='donation'),

    url(r'^donation_submit/$', views.donation_submit, name='donation_submit'),
]
