from django.urls import path
from .views import AddMusician, EditMusician, DeleteMusician

urlpatterns = [
    path('add_musician/', AddMusician.as_view(), name='add_musician'),
    path('edit_musician/<int:id>/', EditMusician.as_view(), name='edit_musician'),
    path('delete_musician/<int:id>/', DeleteMusician.as_view(), name='delete_musician'),
]