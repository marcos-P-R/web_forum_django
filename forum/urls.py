from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path("", views.List.as_view(), name = 'list'),
    path("<int:pk>/", views.Detail.as_view(), name='detail'),
    path("create/", views.Create.as_view(), name='novo-topico'),
]
