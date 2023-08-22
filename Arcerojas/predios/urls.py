from django.urls import path
from .views import list_data, create_owner, create_predio, eliminar_predio

urlpatterns = [
    path('', list_data, name='index'),
    path('save/', create_owner, name='create_owner'),
    path('save_predio/', create_predio, name='create_predio'),
    path('eliminar_predio/<int:id_predio>', eliminar_predio, name='eliminar_predio'),
    #path('editar_predio/<int:id_predio>', editar_predio, name='editar_predio')
]