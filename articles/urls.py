from django.urls import path
from .views import ArticleCreateApi, ArticleApi, ArticleUpdateApi, ArticleDeleteApi


urlpatterns = [
    path('article-create/', ArticleCreateApi.as_view()),
    path('article-view/', ArticleApi.as_view()),
    path('article-update/<int:pk>', ArticleUpdateApi.as_view()),
    path('article-delete/<int:pk>/delete', ArticleDeleteApi.as_view()),
]