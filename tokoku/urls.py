from django.contrib import admin
from django.urls import path
from . import views
from daftar_barang.views import list
from pendaftaran.views import pendaftaran, signup
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', list, name='list'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index),
]
