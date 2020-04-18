from django.urls import path, include

from . import views

# this appname is used inside the html templates   ...for example if we want to get the home url we type articles:home....if you want to get the detail page we type articles:detail

urlpatterns = [
    path("", views.home_page_view.as_view(), name="home_page_view"),
    path("about/", views.about_page_view.as_view(), name="about_page_view"),
]
