from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search_query, name='search'),
    path('', views.index, name='index'),

    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),
]

