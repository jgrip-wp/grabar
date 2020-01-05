# Generated by Django 3.0.1 on 2020-01-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('agent', models.CharField(blank=True, max_length=256)),
                ('industry', models.CharField(max_length=128)),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]
