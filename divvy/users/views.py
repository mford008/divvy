from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from .models import User
from .models import ShareGroup


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ["name"]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserGroupView(LoginRequiredMixin, ListView):
    model = ShareGroup
    username = 'username'

    #def view_all_groups(request, username):
        #context = {
            #'groups': groups,
        #}
        #return render(request, 'pages/all_groups.html', context)

    #def update_groups(request, group_id):
        #new_group = request.POST['group']
        #group = ShareGroup.objects.get(id=group_id)
        #group.new_group = new_group
        #group.save()

        #return render(request, 'pages/all_groups.html', context)
