from django import forms

from forums.models import Category, Topic, Discuss


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('subject', 'body', 'image', 'is_published')


class DiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ('message',)