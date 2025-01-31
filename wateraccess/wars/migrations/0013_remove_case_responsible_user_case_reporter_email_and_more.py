# Generated by Django 5.1.4 on 2024-12-16 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0012_case'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='responsible_user',
        ),
        migrations.AddField(
            model_name='case',
            name='reporter_email',
            field=models.EmailField(default='no-2reply@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='case',
            name='reporter_name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
        migrations.AlterField(
            model_name='case',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='cases/files/'),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='case',
            name='tap_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='case',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL),
        ),
    ]
