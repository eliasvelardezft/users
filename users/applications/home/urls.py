from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'user-panel/',
        views.HomePage.as_view(),
        name='panel'),
    
]