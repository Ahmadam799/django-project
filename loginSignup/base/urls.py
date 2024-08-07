from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),  # Added homepage path  
  path('signup/', views.signup, name='signup'),  
  path("birthdate/", views.birthdateView, name="birthdate"),  
]