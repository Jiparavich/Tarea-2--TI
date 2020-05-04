from django.urls import path
from django.conf.urls import url
from . import views
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('details_chapter/<int:id_capitulo>/', views.details_chapter, name='details_chapter'),
    path('details_character/<int:id_character>/', views.details_character, name='details_character'),
    path('details_location/<int:id_location>/', views.details_location, name='details_location'),
    path('search/', views.search, name='search'),

]"""




urlpatterns = [

    ##gets
    path('hamburguesa', views.hamburguesa_list, name='hamburguesas'),
    path('ingrediente', views.ingrediente_list, name='ingredientes'),
    ##paths y deletes
    path('hamburguesa/<pk>', views.hamburguesa_detail, name='hamburguesa'),
    path('ingrediente/<pk>', views.ingrediente_detail, name='ingrediente'),

    ##diffcult one
    path('hamburguesa/<pk_hamb>/ingrediente/<pk_ingred>', views.ingrediente_hamburguesa, name='ingrediente_hamburguesa'),
]