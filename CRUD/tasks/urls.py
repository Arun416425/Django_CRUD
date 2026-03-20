from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_tasks, name="home"),
    path("create/", views.post_task, name="post_task"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]
