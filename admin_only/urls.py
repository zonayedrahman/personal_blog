from django.urls import path
from . import views


urlpatterns = [


    path('user_admin/', views.user_admin, name='user_admin'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('new/', views.new_article, name='new_article')
]