from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path("", views.List_thread.as_view(), name = 'thread-list'),
    path("<int:pk>/", views.Detail_thread.as_view(), name='detail'),
    path("new/", views.new_thread, name="new-thread"),
    path("delete/<id>", views.delete_thread, name="delete-thread"),
]
