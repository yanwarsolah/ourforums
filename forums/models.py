from django.contrib.auth.models import User
from django.db import models


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_users')
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(TimestampModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='topic_categories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topic_authors')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Discuss(TimestampModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='discuss_topics')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discuss_userss')
    message = models.TextField()

    def __str__(self):
        return self.topic.subject

