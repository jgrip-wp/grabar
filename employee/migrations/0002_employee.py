# Generated by Django 3.0.1 on 2019-12-30 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import employee.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('systemuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('number', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=256)),
                ('name_kana', models.CharField(max_length=256)),
                ('department', models.CharField(choices=[('管理部', '管理部'), ('Webリレーション部', 'Webリレーション部'), ('事業推進室', '事業推進室'), ('クリエイティブ部', 'クリエイティブ部'), ('コンサルティング部', 'コンサルティング部'), ('PR部', 'PR部')], max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=('employee.systemuser',),
            managers=[
                ('objects', employee.models.SystemUserManager()),
            ],
        ),
    ]
