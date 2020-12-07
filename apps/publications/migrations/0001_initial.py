# Generated by Django 2.2.14 on 2020-12-07 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('likes', models.IntegerField()),
                ('comments', models.ManyToManyField(related_name='publications', to='comments.Comment')),
                ('tags', models.ManyToManyField(related_name='publications', to='tags.Tag')),
            ],
        ),
    ]
