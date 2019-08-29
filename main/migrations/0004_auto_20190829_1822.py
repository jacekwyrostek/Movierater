# Generated by Django 2.2.4 on 2019-08-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190823_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='released',
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbRating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
