from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.db.models import Q
from django.urls import reverse

from . models import Article, Comment
from .forms import ArticleForm, CommentForm

# article List View class


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/article_list.html"
    paginate_by = 5
    ordering = "pub_date"

# article search list results view


class ArticleSearchView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/article_search_results.html"
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list

# article details view class


# class ArticleDetailView(LoginRequiredMixin, DetailView):
#     model = Article
#     template_name = "articles/article_detail.html"

def ArticleDetailView(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(
        comment_article=article).order_by('created_on')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                body=form.cleaned_data["body"],
                comment_article=article
            )
            comment.save()

    context = {
        "article": article,
        "comments": comments,
        "form": form
    }
    return render(request, "articles/article_detail.html", context)

# article create view class


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    #fields= ["title", "body"]
    # defines how the html file name will look like
    template_name_suffix = '_create_form'
    # default is model_create_form.html
    # the suffix property defines what the generalshape for the template name is and by default it takes the model name and then we define in the suffix whats next
    # the template_name sets the name manually
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articles:article_list")

# article update view class


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    #fields =["title", "body"]
    template_name_suffix = '_update_form'
    # default is model_update_form.html
    # the suffix property defines what the generalshape for the template name is and by default it takes the model name and then we define in the suffix whats next
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articles:article_list")


# article delete view class
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:article_list')
    # this name home comes from the urls
    # default is author_confirm_delete.html
