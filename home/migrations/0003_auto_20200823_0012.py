# Generated by Django 2.2 on 2020-08-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200823_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='anshou_num',
            field=models.CharField(max_length=4, verbose_name='暗証番号'),
        ),
    ]
