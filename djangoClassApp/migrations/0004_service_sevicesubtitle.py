# Generated by Django 4.2.7 on 2023-11-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoClassApp', '0003_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='seviceSubtitle',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
