# Generated by Django 2.2.2 on 2019-07-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_movie_thumbnail_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='writers',
            field=models.ManyToManyField(blank=True, to='films.Writer'),
        ),
    ]
