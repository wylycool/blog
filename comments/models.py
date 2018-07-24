from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=True,blank=True)
    url = models.URLField(max_length=200,null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    post = models.ForeignKey("blog.Post")

    def __str__(self):
        return self.text[:20]
