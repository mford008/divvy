from django.urls import path

from . import views

app_name = "share-ables"
urlpatterns = [
    path("user_page", view=views.user_page, name="myprofile"),
    path("browse_page", view=views.browse_page, name="browse"),
    
    #we need to add new paths, but this can be done at the end when we have all of our views

    path("", view=views.UserListView.as_view(), name="list"),
    path("~redirect/", view=views.UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=views.UserUpdateView.as_view(), name="update"),
    path(
        "<str:username>/",
        view=views.UserDetailView.as_view(),
        name="detail",
    ),
]



