from django.urls import path
#  imports views from the current app directory
from . import views

# Namespace for this app's URL patterns to avoid conflicts with other apps
app_name = 'my_site'

urlpatterns = [
    # Define URL patterns, mapping routes to views with a name for reverse URL lookup
    path('', views.example_view, name='example'),
    path('variable', views.variable_view, name='variable')
]