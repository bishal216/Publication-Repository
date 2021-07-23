# Generated by Django 3.2.4 on 2021-07-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210627_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
        migrations.AddField(
            model_name='article',
            name='article_link',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='article',
            name='citations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='co_authors',
            field=models.CharField(default=None, help_text='enter coauthors seperated by commas', max_length=200),
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='pages',
            field=models.CharField(blank=True, help_text='must be in form 333-444', max_length=50),
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='article',
            name='publisher',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='volume',
            field=models.IntegerField(default=0),
        ),
    ]
