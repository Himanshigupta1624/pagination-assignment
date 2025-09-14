from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Article
from .serializers import ArticleSerializer
from .pagination import CustomArticlePagination

# Task 1
class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = None 
    max_page_size = 10


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by("-created_at")


# TASK 2
class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by("-created_at") 
    
#TASK 3
class ArticlesListsView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    pagination_class = CustomArticlePagination

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by("-created_at")
 