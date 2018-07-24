from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.


def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            print(post.get_absolute_url())
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                "post":post,
                "form":form,
                "comment_list":comment_list
            }
            return render(request,"blog/index.html",context=context)
    return redirect(post)


