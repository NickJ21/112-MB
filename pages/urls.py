from django.urls import path
from .views import HomePageView, AboutPageView, PostsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name = "about"),
    path("posts/", PostsPageView.as_view(), name = "posts")
]