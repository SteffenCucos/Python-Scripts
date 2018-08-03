from django.urls import path
from rest_framework.authtoken import views as drf_views

from . import views

urlpatterns = [
    path('auth', drf_views.obtain_auth_token, name='auth'),
    path('get_users', views.get_users, name='get_users'),#GET
    path('make_user', views.make_user, name='make_user'),#POST
    path('delete_user', views.delete_user, name='delete_user'),#DELETE
    path('add_subscription', views.add_subscription, name='add_subscription'),#POST
]
