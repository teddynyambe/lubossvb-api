from django.urls import path
from .views import register_user
from .views import login_user
from .views import member_list
from .views import user_member_update

urlpatterns = [
    # Define other URL patterns for your app here

    # URL pattern for the register_user view
    path('member', register_user, name='register_user'),
    path('login', login_user, name='login_user'),
    path('members', member_list, name='member_list'),
    path('member/<uuid:pk>', user_member_update, name='user-member'),
]
