# Generated by Django 4.1.2 on 2022-10-24 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Draft'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.SlugField(max_length=160, unique=True),
        ),
    ]
