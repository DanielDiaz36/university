# Generated by Django 3.2.6 on 2021-08-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercategory',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='usercategory',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='usercategory',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='usercategory',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='usercategory',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='usercategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]