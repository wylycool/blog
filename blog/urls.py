#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>\d{4})/(?P<month>\d{2})/$',views.ArchivesView.as_view(),name='archives'),
    url(r'^category/(?P<pk>\d+)/$',views.CategoryView.as_view(),name='category'),
]