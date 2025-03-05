from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
app_name = 'users'
urlpatterns = [
path('', views.sign_up, name='sign_up'),
path('signout/', LogoutView.as_view(next_page=''), name='logout'),
]