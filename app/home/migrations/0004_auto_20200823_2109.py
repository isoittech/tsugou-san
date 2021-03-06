# Generated by Django 2.2 on 2020-08-23 12:09

import django.core.validators
from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200823_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'イベント情報', 'verbose_name_plural': 'イベント情報'},
        ),
        migrations.AlterModelOptions(
            name='eventkouhonichiji',
            options={'verbose_name': 'イベント候補日時情報', 'verbose_name_plural': 'イベント候補日時情報'},
        ),
        migrations.AlterModelOptions(
            name='sankanichiji',
            options={'verbose_name': '参加日時情報', 'verbose_name_plural': '参加日時情報'},
        ),
        migrations.AlterModelOptions(
            name='sankasha',
            options={'verbose_name': '参加者情報', 'verbose_name_plural': '参加者情報'},
        ),
        migrations.AlterField(
            model_name='event',
            name='anshou_num',
            field=models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4), home.models.only_intger], verbose_name='暗証番号'),
        ),
    ]
