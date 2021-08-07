# Generated by Django 3.2.4 on 2021-07-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title2', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]