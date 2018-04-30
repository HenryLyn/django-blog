from django.db import models
from django.utils.six import python_2_unicode_compatible 

# Create your models here.

"""
@author: HenryLin
@date: 20180422
@desc: comment model
"""
@python_2_unicode_compatible # compatible with python2
class Comment(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255, blank = True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    article = models.ForeignKey('blog.Article',on_delete = models.CASCADE)

    """
    @author: HenryLin
    @date: 20180422
    @desc: return a date for query all data.
    @return:
        comment with first 20 character. -- str
    """
    def __str__(self):
        return self.text[:20]
    
