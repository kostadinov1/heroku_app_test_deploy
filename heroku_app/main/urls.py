from django.urls import path

from heroku_app.main.views import build_home_view

urlpatterns = [
    path('', build_home_view, name='show home')
]