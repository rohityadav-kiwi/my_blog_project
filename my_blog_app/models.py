from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    #
    # def publish(self):
    #     self.published_date = models.DateTimeField(timezone.now)
    #     self.save()
    #     return self.published_date

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
