# Generated by Django 4.0.3 on 2022-04-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_purchase_list',
            name='user_name',
            field=models.CharField(default='hari', max_length=255),
            preserve_default=False,
        ),
    ]
