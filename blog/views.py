from django.shortcuts import render, get_object_or_404

# Create your views here.
# from django.http import HttpResponse
from .models import Article, Category
from markdown import markdown
from comment.forms import CommentForm

"""
@author: Henry Lin
@date: 20180418
@desc: populate indext html and return index html
@param:
    request: http request
@return:
    index html
"""
def index(request):
    article_list = Article.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context = {
        'article_list' : article_list
    })

"""
@author: Henry Lin
@date: 20180418
@desc: populate detail information and return detail html
@param:
    request: http request
    pk: article primary key
@return:
    detail html
"""
def detail(request, pk):
    article = get_object_or_404(Article, pk = pk)
    article.body = markdown(article.body, extensions = ['markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc'])
    form = CommentForm()
    comment_list = article.comment_set.all()
    return render(request, 'blog/detail.html', context = { 'article' : article,
                                                           'form' : form,
                                                           'comment_list' : comment_list })

"""
@author: Henry Lin
@date: 20180419
@desc: get archived articles.
@param: 
    request: http request
    year: year.
    month: month. 
@return:
    article_list.
"""
def archives(request, year, month):
    article_list = Article.objects.filter(create_time__year = year,
                                          create_time__month = month
                                          ).order_by('-create_time')
    return render(request, 'blog/index.html', context = { 'article_list' : article_list })

"""
@author: Henry Lin
@date: 20180419
@desc: get current category articles.
@param:
    request: http request. -- HttpRequest
    pk: article category primary key. --  string
@return:
    article_list
"""
def category(request, pk):
    category = get_object_or_404(Category, pk = pk)
    article_list = Article.objects.filter(category = category).order_by('-create_time')
    return render(request, 'blog/index.html', context = { 'article_list' : article_list })
