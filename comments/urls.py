#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from django.conf.urls import url
from comments import views


app_name = "comments"
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>\d+)/$',views.post_comment,name="post_comment")
]