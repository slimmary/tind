# Generated by Django 2.2.24 on 2021-12-14 21:46

from django.db import migrations, models
import django.db.models.deletion
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20211214_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=photos.models.upload_gallery_image)),
                ('description', models.CharField(blank=True, help_text='Enter short text description', max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='users.UserProfile')),
            ],
        ),
    ]
