from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .models import Comment
from .forms import CommentForm

# Create your views here.
"""
@author: HenryLin
@date: 20180422
@desc: analysis comment
"""
def article_comment(request, pk):
    article = get_object_or_404(Article, pk = pk)
    # check if not post request.
    if not (request.method == 'POST'):
        print("not post")
        return redirect(article)
    
    form = CommentForm(request.POST)
    # check if data is valid
    if form.is_valid():
        # set commit = False means only create the comment object, but did not save into database.
        comment = form.save(commit = False)
        comment.article = article
        comment.save()
        print("save")
        return redirect(article)
    else:
        comment_list = article.comment_set.all()
        context = {'article' : article,
                   'form' : form,
                   'comment_list' : comment_list
        }
        print("not save")
        return render(request, 'blog/detail.html', context = context)
        
