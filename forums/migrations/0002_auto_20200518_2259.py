# Generated by Django 3.0.6 on 2020-05-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discuss',
            name='message',
            field=models.TextField(),
        ),
    ]
