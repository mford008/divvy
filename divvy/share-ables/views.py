from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

from .models import ShareItem

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'owner', 'availability', 'timeframe']

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'availability', 'timeframe']
        
        
def post_page(request):
    if request.method == 'POST':
    
        form = NewItemForm(request.POST)
        
        if form.is_valid():
            item = form.save()
            
            auth.login(request, user)
            return redirect('/')
    
    else:
        form = NewItemForm()
        
    context = {
        'form': form,
    }
    return render(request, 'pages/post.html', context)
    
    
def browse_page(request):
    if request.method == 'GET':
    

