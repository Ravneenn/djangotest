# Generated by Django 3.2.25 on 2024-07-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_article_langs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='langs',
            field=models.ManyToManyField(to='library.Language'),
        ),
    ]
