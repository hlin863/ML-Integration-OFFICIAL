from celery import shared_task

from .models import Post

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_posts():
    return Post.objects.count()


@shared_task
def rename_post(post_id, title):
    post = Post.objects.get(id=post_id)
    post.title = title
    post.save(update_fields=["title"])


@shared_task
def count_widgets():
    return Post.objects.count()


@shared_task
def rename_widget(widget_id, name):
    post = Post.objects.get(id=widget_id)
    post.title = name
    post.save(update_fields=["title"])

