# Generated by Django 5.0.2 on 2024-03-02 19:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_blogmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReaderProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Age', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('recent_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.blogmodel')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='writterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Age', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('recent_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.blogmodel')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
