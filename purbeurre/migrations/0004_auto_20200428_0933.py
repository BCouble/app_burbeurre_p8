# Generated by Django 3.0.5 on 2020-04-28 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0003_categorys0_categorys1_categorys2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys0',
            name='name_cat_s0',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categorys1',
            name='name_cat_s1',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='CategoryS2',
        ),
    ]
