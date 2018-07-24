import math
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post,Category
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView,DetailView

# 定义判断分页的函数
def custompaginator(num_page,current_page,max_page):
    # 获取中间值
    middle = math.ceil(max_page/2)
    #判断，当页面最大数小于最大页面显示数
    if num_page < max_page:
        start = 1
        end = num_page
    else:
        # 当前页小于等于middle+1时候
        if current_page <= middle +1:
            start = 1
            end = max_page
        else:
            start = current_page - middle
            end = current_page + middle -1
            # 当前页在尾部的时候
            if current_page + middle > num_page:
                start = num_page - middle -1
                end = num_page
    return start,end

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 2

    # 增加额外的context内容
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        start,end = custompaginator(paginator.num_pages,page.number,3)
        context.update({
            'page_range':range(start,end+1)
        })
        return context
# def index(request):
#     post_list = Post.objects.all().order_by('-create_time')
#     return render(request, "blog/index.html", locals())

# 详细页面
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    # 覆写get方法
    def get(self, request, *args, **kwargs):
        # 先调用父类的get方法，self.object属性中才会有Post模型的实例。
        response = super().get(request, *args, **kwargs)
        # 文章阅读量+1
        # self.object的值就是被访问的文章对象post
        self.object.increase_view()
        return response
    # 复写get_object方法的目的是因为需要对post的body值进行渲染
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body,extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context
'''
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_view()
    form = CommentForm()
    comment_list = post.comment_set.all()
    post.body = markdown.markdown(post.body,extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return render(request,'blog/detail.html',locals())
'''
# 归档
class ArchivesView(IndexView):
    def get_queryset(self):
        return super().get_queryset().filter(
            create_time_year = self.kwargs.get('year'),
            create_time_month = self.kwargs.get('month')
        )
# def archives(request,year,month):
#     post_list = Post.objects.filter(create_time__year=year,create_time__month=month).order_by("-create_time")
#     return render(request,'blog/index.html',locals())

#分类
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk = self.kwargs.get("pk"))
        return super().get_queryset().filter(category = cate)
# def get_category(request,pk):
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by("-create_time")
#     return render(request,"blog/index.html",{"post_list":post_list})
