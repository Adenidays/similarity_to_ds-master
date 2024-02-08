
from django.urls import path

from userapp.views import GetAllUsersView

urlpatterns = [
    path('get_all_user/',GetAllUsersView.as_view(), name='message-list'),
]