from django.urls import path
from .views import AddAlbum, EditAlbum, DeleteAlbum

urlpatterns = [
    path('add_album/', AddAlbum.as_view(), name='add_album'),
    path('edit_album/<int:id>/', EditAlbum.as_view(), name='edit_album'),
    path('delete_album/<int:id>/', DeleteAlbum.as_view(), name='delete_album'),
]