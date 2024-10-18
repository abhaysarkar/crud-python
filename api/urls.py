from django.urls import path
from home.views import delete_user_by_email, editRegisteredUser, get_all_users, get_user_by_email, index, register

urlpatterns = [
  path('index/', index),  
  path('register/', register),
  path('edituser/', editRegisteredUser),
  path('getalluser/', get_all_users),
  path('getuser/<email>', get_user_by_email),
  path('deletuserbyemail/', delete_user_by_email),
]