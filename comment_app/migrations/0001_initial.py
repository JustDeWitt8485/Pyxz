# Generated by Django 3.1.5 on 2021-01-05 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photo_app', '0002_auto_20210105_1948'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='comementlikes', to=settings.AUTH_USER_MODEL)),
                ('photo_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_linked', to='photo_app.image')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
