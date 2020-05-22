# Generated by Django 3.0.6 on 2020-05-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('comment', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
