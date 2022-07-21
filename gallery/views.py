from django.shortcuts import render
from django.views.generic import ListView, DetailView
from gallery.models import Image


class ImageListView(ListView):

    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context, "Context")
        return context

class ImageDetailView(DetailView):

    model = Image
    # context_object_name = 'image'
    # queryset = Image.objects.all()
    #

    def get_object(self):
        obj = super().get_object()
        print("tsar")
        return obj
