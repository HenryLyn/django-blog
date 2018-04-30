from ..models import Article, Category
from django import template

# register register
register = template.Library()

"""
@author: Henry Lin
@date: 20180419
@desc: get neweast article from database
@param:
    num: number of articles. -- int
@return:
    articles: article objects. -- Article list
"""
@register.simple_tag # register template tag into django
def get_recent_article(num = 5):
    return Article.objects.all().order_by('-create_time')[ : num]

"""
@author: Henry Lin
@date: 20180419
@desc: get archived article date
@return:
    date: articles date by year and month. -- list
"""
@register.simple_tag
def get_archived_date():
    return Article.objects.dates('create_time', 'month', order = 'DESC')

"""
@author: Henry Lin
@date: 20180419
@desc: get article category
@return:
    categorys: article categories. -- list
"""
@register.simple_tag
def get_article_categories(num = 10):
    return Category.objects.all().order_by('-pk')[ : num]
