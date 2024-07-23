# Generated by Django 3.2.25 on 2024-07-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_work_workstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='work',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='workstatus',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]