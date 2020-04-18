from django.contrib import admin
from .models import Article, ArticleCategory, ArticleSeries, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ArticleAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Article, ArticleAdmin)

admin.site.register(ArticleCategory)

admin.site.register(ArticleSeries)

admin.site.register(Comment)
