# Generated by Django 3.2.5 on 2021-09-12 16:49

import datetime
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
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, verbose_name='Heading')),
                ('details', models.TextField(verbose_name='Details')),
                ('img', models.ImageField(upload_to='static/media/contests')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('commentsCnt', models.IntegerField(default=0, verbose_name='Comments Count')),
                ('result', models.FileField(blank=True, null=True, upload_to='static/media/result')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(verbose_name='Comment Details')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('contestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentOwner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
