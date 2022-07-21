from django.urls import path
from gallery.views import ImageListView, ImageDetailView

urlpatterns = [

    path("images/", ImageListView.as_view(), name="images"),
    path("images/<int:pk>", ImageDetailView.as_view(), name="image-detail"),
    path("images/new", ImageDetailView.as_view(), name="image-detail"),

]
