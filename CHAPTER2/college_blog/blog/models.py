from django.db import models
from django.db.models.functions import Now
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
class Post(models.Model):
    # //Q1
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    body=models.TextField()
    # //Q2
    publish=models.DateTimeField(db_default=Now())
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-publish']
        indexes=[models.Index(fields=['-publish']),
                ]
        
    # Q3
    class Status(models.TextChoices):
        DRAFT='DF','Draft'
        PUBLISHED='PB','Published'


    status=models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Post'
    )
    objects=models.Manager()
    published=PublishedManager()
    def __str__(self):
        return self.title
    

    # Q4
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
                # self.id
                ]
        )
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,
    related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'