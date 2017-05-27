from django.http import Http404
from django.shortcuts import render
from .models import Donation


def index(request):
    some_value = 'Test value'
    context = {
        'some_value': some_value
    }
    return render(request, 'ffutche/index.html', context)


def donation(request):
    some_value = 'Test value'
    context = {
        'some_value': some_value
    }
    return render(request, 'ffutche/donation.html', context)

def donation_submit(request):
    contributor_name = request.POST['contributor_name']
    phone_number = request.POST['phone_number']
    email_id = request.POST['email_id']
    contribution_type = request.POST['contribution_type']
    quantity = request.POST['quantity']
    value = request.POST['value']

    contribution = Donation()
    contribution.contributor_name = contributor_name
    contribution.phone_number = phone_number
    contribution.email_id = email_id
    contribution.contribution_type = contribution_type
    contribution.quantity = quantity
    contribution.value = value
    contribution.save()

    return render(request, 'ffutche/donation.html', {'message': "Thank you for the donation."})
