# Generated by Django 3.0.5 on 2020-05-24 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0010_remove_favoris_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoris',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purbeurre.FoodPurBeurre', unique=True),
        ),
    ]
