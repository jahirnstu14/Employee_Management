

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.user_list,name='user_list'),
    path('Add/', views.AddUser,name='add_user'),
    path('Edit/<id>', views.EditUser, name='edit_user'),
    path('Delete/<eid>', views.DeleteUser, name='delete_user'),
    path('View/<eid>', views.ViewUser, name='view_user'),
]