# Generated by Django 3.0.7 on 2020-06-08 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_auto_20200605_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioproject',
            old_name='image1',
            new_name='image',
        ),
    ]
