from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

"""
@author: Henry Lin
@date: 20180416
@desc: a class mapping with database table, named CATEGORY.
"""
class Category(models.Model): # model must extends models.Model
    # CharField means 
    name = models.CharField(max_length = 50)

    """
    @author: Henry Lin
    @date: 20180417
    @desc: return category name for query all
    @return:
        name: category name. -- string
    """
    def __str__(self):
        return self.name
    
"""
@author: Henry Lin
@date: 20180416
@desc: a class mapping with database table, named TAG.
"""
class Tag(models.Model):
    name = models.CharField(max_length = 50)

    """
    @author: Henry Lin
    @date: 20180417
    @desc: return tag name for query all
    @return:
        name: tag name. -- string
    """
    def __str__(self):
        return self.name
    
"""
@author: Henry Lin
@date: 20180416
@desc: a class mapping with database table, named Article
"""
class Article(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 300, blank = True)

    # Relationships with tag and category.
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag, blank = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    """
    @author: Henry Lin
    @date: 20180417
    @desc: return Article title for query all.
    @return
        title: article title. -- string
    """
    def __str__(self):
        return self.title

    """
    @author: Henry Lin
    @date: 20180418
    @desc: get absolute url
    @return:
        url: url. -- string
    """
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs = { 'pk' : self.pk})
