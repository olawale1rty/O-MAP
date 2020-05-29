from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('incidence/', views.Incidence_data, name='incidence'),
	path('country/', views.Country_data, name='country'),
]