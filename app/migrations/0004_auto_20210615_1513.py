# Generated by Django 3.2 on 2021-06-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_tittle_question_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='count',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Tag'),
        ),
    ]
