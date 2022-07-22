from django.urls import path
from gallery.views import ImageListView, ImageDetailView, ImageCreateView, ImageUpdateView, delete_image
from utils.constant import URLS

urlpatterns = [

    path("", ImageListView.as_view(), name=URLS.IMAGE_LIST),
    path("show/<int:pk>", ImageDetailView.as_view(), name=URLS.IMAGE_DETAILS),
    path("new", ImageCreateView.as_view(), name=URLS.NEW_IMAGE),
    path("<int:pk>/edit", ImageUpdateView.as_view(), name=URLS.UPDATE_IMAGE),
    path("<int:pk>/delete", delete_image, name=URLS.DELETE_IMAGE),

]
