from django.urls import path
from gallery.views import ImageListView, ImageDetailView, ImageCreateView, ImageUpdateView, ImageDeleteView
from utils.constant import URLS

urlpatterns = [

    path("images/", ImageListView.as_view(), name=URLS.IMAGE_LIST),
    path("images/<int:pk>", ImageDetailView.as_view(), name=URLS.IMAGE_DETAILS),
    path("images/new", ImageCreateView.as_view(), name=URLS.NEW_IMAGE),
    path("images/<int:pk>/update", ImageUpdateView.as_view(), name=URLS.UPDATE_IMAGE),
    path("images/<int:pk>/delete", ImageDeleteView.as_view(), name=URLS.DELETE_IMAGE),

]
