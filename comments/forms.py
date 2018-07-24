#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name","email","url","text"]