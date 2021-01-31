from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:company_slug>/', views.show_company, name='show_company'),
    path('<slug:company>/<int:person_pk>/', views.show_profile, name='show_profile'),
]
