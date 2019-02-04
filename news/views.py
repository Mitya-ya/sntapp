from django.shortcuts import render
from django.utils import timezone
from news.models import Post

# Create your views here.

def news_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'news/news_list.html', {'posts': posts})
