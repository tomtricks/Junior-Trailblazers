# Generated by Django 4.0.2 on 2022-04-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryblog', '0015_post_register_url_alter_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='register_url',
            field=models.CharField(default='www.google.com', max_length=255, null=True),
        ),
    ]
