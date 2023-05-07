from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from articles.documents import ArticleDocument
from rest_framework import generics
from .models import Article
from .serializers import ArticleDocumentSerializer, ArticleSerializer


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend
    ]

    search_fields = (
        'title',
    )

    filter_fields = {
        'category': 'category.id'
    }

    suggester_fields = {
        'title': {
              'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    },


class ArticleCreateApi(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleApi(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteApi(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer