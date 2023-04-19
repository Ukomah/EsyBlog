from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Article
# Create your views here.
class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 1




