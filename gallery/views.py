from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gallery.forms import ImageCreationForm
from gallery.models import Image


class ImageListView(ListView):

    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # context_object_name = 'books'
    # paginate_by = 5
    #
    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     books = self.get_queryset()
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(books, self.paginate_by)
    #     try:
    #         books = paginator.page(page)
    #     except PageNotAnInteger:
    #         books = paginator.page(1)
    #     except EmptyPage:
    #         books = paginator.page(paginator.num_pages)
    #     context['books'] = books
    #     return context

class ImageDetailView(DetailView):

    model = Image
    # context_object_name = 'image'

    def get_object(self):
        obj = super().get_object()
        return obj


class ImageCreateView(CreateView):

    model = Image
    fields = ["name", "url", "detail"]
    success_url = reverse_lazy('images')


class ImageUpdateView(UpdateView):

    model = Image
    fields = ["name", "url", "detail"]
    success_url = reverse_lazy('images')

    def get_success_url(self):
        return reverse_lazy('image-detail', kwargs={'pk': self.object.id})


class ImageDeleteView(DeleteView):

    model = Image
    success_url = reverse_lazy('images')



