# Generated by Django 3.0.1 on 2020-01-01 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail/'),
        ),
    ]
