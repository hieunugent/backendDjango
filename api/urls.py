from django.urls import path
from .views import UserList

urlpatterns = [
     path('users/', UserList.as_view(), name='user_list'),
    # path('users/', views.user_list, name='user_list'),
    # path('users/add/', views.add_user, name='add_user'),
]
