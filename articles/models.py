from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class ArticleCategory(models.Model):
    article_category = models.CharField(max_length=200)
    article_summary = models.CharField(max_length=200)
    article_slug = models.CharField(max_length=200)

    class Meta:
        # this is for the admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.article_category


class ArticleSeries(models.Model):
    article_series = models.CharField(max_length=200)
    article_category = models.ForeignKey(
        ArticleCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.article_series


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             related_name="publisher", on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # categories = models.ManyToManyField(
    #     'ArticleSeries', related_name="article")

    tutorial_series = models.ForeignKey(
        ArticleSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_list')
    # if we want the absolute url to redirect to a detail page for examplel
    # def get_absolute_url(self):
    #    return reverse('detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    comment_article = models.ForeignKey(
        'Article', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.author
