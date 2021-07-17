from django.urls import path

from app.views import post_list

urlpatterns = [
    path('list', post_list)
]
