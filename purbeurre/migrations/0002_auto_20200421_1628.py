# Generated by Django 3.0.5 on 2020-04-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='background',
            field=models.CharField(choices=[('1', 'Rose'), ('2', 'Vert'), ('3', 'Orange')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='genre',
            field=models.CharField(choices=[('F', 'femme'), ('M', 'homme'), ('O', 'non définit')], default='O', max_length=2),
        ),
    ]
