# Generated by Django 3.2.6 on 2021-08-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'User category',
                'verbose_name_plural': 'User categories',
                'db_table': 'core_user_category',
                'ordering': ['category'],
            },
        ),
    ]
