from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

from .models import ShareItem
import requests
import os


class NewItemForm(forms.ModelForm):
    class Meta:
        model = ShareItem
        fields = ['item_name', 'avail_time', 'borrow_time', 'descript', 'image']


def upload(request):
    # CREATE item listing
    if request.method == 'POST':

        # i think we need to replace these forms with the ones CC made for us
        # i'm not sure how to go about doing that yet
        form = NewItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.username = request.user
            item.save()

            return redirect(request.META.get('HTTP_REFERER', '/'))

    else:
        # if a GET request, give them a blank form?
        form = NewItemForm()
    items = ShareItem.objects.all()
    context = {
        'form': form,
        'items': items,           # but make it into a for loop? with the tiles like on browse.html
    }

    # this return might be in the wrong spot
    return render(request, 'pages/upload.html', context)


def browse_page(request):
    # Populates the browse page with fake items for users to 'borrow'
    items = ShareItem.objects.all()
    context = {
        'image_src': ShareItem.image,
        'items': items,
    }

    return render(request, 'pages/browse.html', context)


# this def should be okay, but we wont know till all the rest of the code is working
def delete_item(request, item_id):
    item = ShareItem.objects.get(id=item_id)
    item.delete()

    # redirects to page where they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


def update_item(request, item_id):
    # this code is incomplete, ['fields'] needs to be changed
    # its supposed to retrieve the fields they want to update from the update form
    update = request.POST['fields']

    # this code should work, it takes the current item and all the fields
    # and replaces it with the new, updated item
    item = ShareItem.objects.get(id=item_id)
    item.update = update
    item.save()

    # redirects to page where they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))


def send_email(request):
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]

    mailgun_api_key = os.environ['MAILGUN_API_KEY']

    requests.post(
        "https://api.mailgun.net/v3/sandbox5b2a8563d7804446a51e0188857ff46b.mailgun.org/messages",
        auth=("api", mailgun_api_key),

        data={
            "from": "divvy@borrow.com",
            "to": [email, "@sandbox5b2a8563d7804446a51e0188857ff46b.mailgun.org"],
            "subject": "Can I borrow your stuff? From: " + name,
            "text": message,
            })

    return redirect(request.META.get('HTTP_REFERER', '/'))
