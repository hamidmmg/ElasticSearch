from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from articles.views import ArticleDocumentView, ArticleApi

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'article-search', ArticleDocumentView, basename='article-search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]

urlpatterns += router.urls