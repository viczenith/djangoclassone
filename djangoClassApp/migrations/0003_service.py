# Generated by Django 4.2.7 on 2023-11-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoClassApp', '0002_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=20000)),
            ],
        ),
    ]