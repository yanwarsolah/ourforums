# Generated by Django 3.0.6 on 2020-05-15 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_authors', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_categories', to='forums.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=200)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discuss_topics', to='forums.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discuss_userss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
