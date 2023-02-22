# Generated by Django 4.1.5 on 2023-02-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justix', '0008_main_class_class_main_class_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=100, verbose_name='Logo')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('service_text', models.TextField(blank=True, verbose_name='Text')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]