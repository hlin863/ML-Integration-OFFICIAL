# define Widget model
from django.db import models

# import reverse
from django.urls import reverse

class Widget(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # implement the get_absolute_url method
    def get_absolute_url(self):
        return reverse('blog:widget_detail', kwargs={'pk': self.pk})

    def reverse(self):
        return reverse('blog:widget_detail', kwargs={'pk': self.pk})

    def reverse(self, url):
        return reverse(url, kwargs={'pk': self.pk})

