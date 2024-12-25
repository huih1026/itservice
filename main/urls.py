from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='/main/home')),
    path('home/', views.home, name='home'),
    # path('create_cash_entry/', views.create_cash_entry, name='create_cash_entry'),
]