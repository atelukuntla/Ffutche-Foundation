from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Donation
from .forms import UserForm


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


class UserFormView(View):
    form_class = UserForm
    template_name = 'ffutche/registration_form.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process registration form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Clean (normalize) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user object if cred are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
