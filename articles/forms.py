from django import forms
from articles.models import Article, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", 'body']
        widgets = {
            'body': SummernoteWidget(),
            # 'body': SummernoteInplaceWidget()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', "email", "body"]


# class CommentForm(forms.Form):
#     author = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder": "Your Name"
#         })
#     )

#     email = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder": "Your Email"
#         })
#     )

#     body = forms.CharField(
#         widget=forms.Textarea(attrs={
#             "class": "form-control",
#             "placeholder": "Your Name"
#         })
#     )
