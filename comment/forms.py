from django import forms
from .models import Comment

"""
@author: HenryLin
@date: 20180422
@desc: create a form for adding comment
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']
