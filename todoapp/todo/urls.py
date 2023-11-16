from django.urls import path
from.views import CustomLoginView, Taskcreate,RegisterPage,Tasklist,TaskDetailview,TaskUpdate,TaskDelete
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('taskcreate/',Taskcreate.as_view(),name='create'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',CustomLoginView.as_view(),name='login'),
    path('tasklist/',Tasklist.as_view(),name='task'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('task-details/<int:pk>/',TaskDetailview.as_view(),name='detailview'),
    path('update/<int:pk>/',TaskUpdate.as_view(),name='edit'),
    path('delete/<int:pk>/',TaskDelete.as_view(),name='del'),
]
