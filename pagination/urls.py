from django.urls import path
from .views import ArticleListView,ArticlesListView,ArticlesListsView

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles-v2/", ArticlesListView.as_view(), name="articles-list"),
    path("articles-v3/", ArticlesListsView.as_view(), name="articles-lists"),
]
