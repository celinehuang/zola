# Generated by Django 3.0.4 on 2020-04-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vueapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
