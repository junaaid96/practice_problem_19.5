from .models import Album
from . import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.


@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    model = Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Album Created Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data!")
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView):
    model = Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Album Updated Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data!")
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, "Album Deleted Successfully!")
        return reverse_lazy('home')
