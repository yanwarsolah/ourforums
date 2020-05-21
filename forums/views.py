from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

from forums.filters import CategoryFilter, TopicFilter
from forums.forms import CategoryForm, TopicForm, DiscussForm
from forums.models import Category, Topic, Discuss


def category_list(request):
    categories = Category.objects.annotate(
        total=Count('topic_categories')
    ).order_by('-total', '-created')

    total = categories.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(categories, 10)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'total': total
    }

    return render(request, 'forums/category_list.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.slug = slugify(obj.name)
            obj.save()
            return redirect('forums:category_list')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, 'forums/category_create.html', context=context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def category_edit(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(obj.name)
            obj.user = request.user
            obj.save()
            return redirect('forums:category_list')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'forums/category_edit.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def category_search(request):
    categories = Category.objects.annotate(
        total=Count('topic_categories')
    ).order_by('-total', '-created')
    search = ','.join([
        request.GET.get('name', ''),
        request.GET.get('user__username', '')
    ])
    categories = CategoryFilter(request.GET, queryset=categories).qs
    total = categories.count()

    context = {
        'categories': categories,
        'total': total,
        'search': search
    }

    return render(request, 'forums/category_search.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def topic_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    topics = Topic.objects.filter(
        category=category
    ).annotate(
        total_discuss=Count('discuss_topics')
    ).order_by('total_discuss', '-created')

    topics = TopicFilter(request.GET, queryset=topics).qs
    total = topics.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(topics, 10)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    context = {
        'topics': topics,
        'total': total,
        'category': category
    }

    return render(request, 'forums/topic_list.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def topic_search(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    topics = Topic.objects.filter(
        category=category
    ).annotate(
        total_discuss=Count('discuss_topics')
    ).order_by('total_discuss', '-created')

    topics = TopicFilter(request.GET, queryset=topics).qs
    total = topics.count()

    context = {
        'topics': topics,
        'total': total,
        'category': category
    }

    return render(request, 'forums/topic_search.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def topic_create(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(f'{obj.subject} {obj.created}')
            obj.author = request.user
            obj.category = category
            obj.save()
            return redirect('forums:topic_list', category_slug=category.slug)
    else:
        form = TopicForm()

    context = {
        'category': category,
        'form': form,
    }

    return render(request, 'forums/topic_create.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def topic_edit(request, category_slug, slug):
    category = get_object_or_404(Category, slug=category_slug)
    topic = get_object_or_404(Topic, slug=slug)

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES, instance=topic)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = slugify(f'{obj.subject} {obj.created}')
            obj.category = category
            obj.save()
            return redirect('forums:topic_list', category_slug=category.slug)
    else:
        form = TopicForm(instance=topic)

    context = {
        'category': category,
        'topic': topic,
        'form': form,
    }

    return render(request, 'forums/topic_edit.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def topic_detail(request, category_slug, slug):
    category = get_object_or_404(Category, slug=category_slug)
    topic = get_object_or_404(Topic, slug=slug)
    discusses = Discuss.objects.filter(topic=topic).order_by('-created')

    total = discusses.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(discusses, 10)
    try:
        discusses = paginator.page(page)
    except PageNotAnInteger:
        discusses = paginator.page(1)
    except EmptyPage:
        discusses = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = DiscussForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.topic = topic
            obj.user = request.user
            obj.save()

            return redirect('forums:discuss_send_congratulation',
                            category_slug=category_slug, slug=slug)
    else:
        form = DiscussForm()

    context = {
        'category': category,
        'topic': topic,
        'form': form,
        'discusses': discusses,
        'total': total,
    }

    return render(request, 'forums/topic_detail.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def discuss_delete(request, category_slug, slug, pk):
    discuss = get_object_or_404(Discuss, pk=pk)
    topic = get_object_or_404(Topic, slug=slug)
    category = get_object_or_404(Category, slug=category_slug)

    if request.method == 'POST':
        discuss.delete()
        return redirect('forums:topic_detail',
                        category_slug=category_slug, slug=slug)

    context = {
        'discuss': discuss,
        'topic': topic,
        'category': category
    }

    return render(request, 'forums/discuss_delete.html', context)


@login_required(login_url=reverse_lazy('accounts:need_signin'))
def discuss_send_congratulation(request, category_slug, slug):
    category = get_object_or_404(Category, slug=category_slug)
    topic = get_object_or_404(Topic, slug=slug)

    context = {
        'category': category,
        'topic': topic,
    }

    return render(request, 'forums/congrats/discuss_send_congratulation.html', context)
