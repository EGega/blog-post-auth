# Generated by Django 4.1.4 on 2022-12-31 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]