# Generated by Django 3.2.4 on 2021-06-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrain_manager', '0003_alter_terrain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
