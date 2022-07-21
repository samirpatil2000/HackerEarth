from django.urls import path
from gallery.views import ImageListView, ImageDetailView, ImageCreateView, ImageUpdateView

urlpatterns = [

    path("images/", ImageListView.as_view(), name="images"),
    path("images/<int:pk>", ImageDetailView.as_view(), name="image-detail"),
    path("images/new", ImageCreateView.as_view(), name="image-new"),
    path("images/<int:pk>/update", ImageUpdateView.as_view(), name="image-update"),
    path("images/<int:pk>/delete", ImageUpdateView.as_view(), name="image-delete")

]
