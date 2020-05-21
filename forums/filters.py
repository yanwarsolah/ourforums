import django_filters

from forums.models import Category, Topic


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name', 'user__username',]


class TopicFilter(django_filters.FilterSet):
    class Meta:
        model = Topic
        fields = ['subject', 'author__username']