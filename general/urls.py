from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("article/<int:article_id>/", views.view_article, name='article_detail')
]