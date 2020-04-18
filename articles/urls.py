from django.urls import path, include

from . import views

# this appname is used inside the html templates   ...for example if we want to get the home url we type articles:home....if you want to get the detail page we type articles:detail
app_name = "articles"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),

    path("article/<int:pk>", views.ArticleDetailView,
         name="article_detail"),

    path("search-results/", views.ArticleSearchView.as_view(), name="search_results"),

    path('article/create', views.ArticleCreateView.as_view(), name='add_article'),

    path('article/update/<int:pk>',
         views.ArticleUpdateView.as_view(), name='edit_article'),

    path('article/delete/<int:pk>',
         views.ArticleDeleteView.as_view(), name="delete_article"),
]
