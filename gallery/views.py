from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from utils.constant import URLS
from gallery.forms import ImageCreationForm
from gallery.models import Image


class ImageListView(ListView):

    model = Image
    context_object_name = 'images'
    paginate_by = 1
    template_name = 'gallery/image_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(images, self.paginate_by)
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)
        context['images'] = images
        return context


# def image_list(request):


class ImageDetailView(DetailView):

    model = Image
    # context_object_name = 'image'

    def get_object(self):
        obj = super().get_object()
        return obj


class ImageCreateView(CreateView):

    model = Image
    fields = ["name", "url", "detail"]
    success_url = reverse_lazy(URLS.IMAGE_LIST)


class ImageUpdateView(UpdateView):

    model = Image
    fields = ["name", "url", "detail"]
    success_url = reverse_lazy(URLS.IMAGE_LIST)

    def get_success_url(self):
        return reverse_lazy(URLS.IMAGE_DETAILS, kwargs={'pk': self.object.id})

def delete_image(request, pk):
    try:
        image_object = Image.objects.get(pk=pk)
        image_object.delete()
    except ObjectDoesNotExist:
        pass
    return redirect(URLS.IMAGE_LIST)



