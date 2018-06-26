from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

from .models import ShareItem


# these two forms are templated from the Twitten activity, we might not need them
class NewItemForm(forms.ModelForm):
    class Meta:
        model = ShareItem
        fields = ['item_name', 'username', 'available', 'borrow_time', 'image']


class EditItemForm(forms.ModelForm):
    class Meta:
        model = ShareItem
        fields = ['item_name', 'available', 'borrow_time', 'image']


def user_page(request, username):
    user = User.objects.get(username=username)
    #CREATE item listing
    if request.method == 'POST':

        # i think we need to replace these forms with the ones CC made for us
        # i'm not sure how to go about doing that yet
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()

            return redirect(request.META.get('HTTP_REFERER', '/'))

    else:
        #if a GET request, give them a blank form?
        form = NewItemForm()

    #READ all items that this user has posted
    items = ShareItem.objects.order_by('-created')
    items_by_user = items.filter(user=user)

    context = {
        'items': items_by_user, #this needs to be inserted into html like: {{ items }}
        'form': form,           #but make it into a for loop? with the tiles like on browse.html
        'user_on_page': user,
        'is_me': user == request.user,
    }

    # this return might be in the wrong spot
    return render(request, 'templates/users/user_detail.html', context)



def browse_page(request):
    if request.method == 'GET': #'GET' might be wrong too, but this page is a view only page
                                # so it made sense in my head...

        # i think this part is wrong, my goal is to authenticate the user/group
        # before displaying the items they are 'allowed' to see
        if auth.login(request, user)
            context = {
                'share-ables': all_items,
                'user_on_page': user,
                'is_me': user == request.user,
            }
            return render(request, 'pages/browse.html', context)

    else:
        #redirects to page where they came from
        return redirect(request.META.get('HTTP_REFERER', '/'))


#this def should be okay, but we wont know till all the rest of the code is working
def delete_item(request, item_id):
    item = ShareItem.objects.get(id=item_id)
    item.delete()

    #redirects to page where they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))



def update_item(request, item_id):
    #this code is incomplete, ['fields'] needs to be changed
    #its supposed to retrieve the fields they want to update from the update form
    update = request.POST['fields']

    #this code should work, it takes the current item and all the fields
    #and replaces it with the new, updated item
    item = ShareItem.objects.get(id=item_id)
    item.update = update
    item.save()

    #redirects to page where they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))