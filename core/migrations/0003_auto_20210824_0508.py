# Generated by Django 3.2.6 on 2021-08-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210824_0300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'default_permissions': [], 'ordering': ('created_at',), 'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
        migrations.RemoveField(
            model_name='student',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='student',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
