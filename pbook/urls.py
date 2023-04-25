
from django.contrib import admin
from django.urls import path
from core.views import index, users

urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
    path('admin/', admin.site.urls),
]
