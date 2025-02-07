# Generated by Django 4.0.3 on 2022-03-31 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads_catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=30)),
                ('company_email', models.CharField(max_length=50, unique=True)),
                ('company_password', models.CharField(max_length=50)),
                ('ad_price', models.IntegerField()),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_signup.ads_catagory')),
            ],
        ),
    ]
