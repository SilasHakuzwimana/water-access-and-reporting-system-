# Generated by Django 5.1.4 on 2024-12-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0013_remove_case_responsible_user_case_reporter_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/contacts/'),
        ),
    ]