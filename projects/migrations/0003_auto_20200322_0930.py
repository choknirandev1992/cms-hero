# Generated by Django 3.0.4 on 2020-03-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200321_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(blank=True),
        ),
    ]
