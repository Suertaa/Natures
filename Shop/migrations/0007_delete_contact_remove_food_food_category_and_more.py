# Generated by Django 4.2.1 on 2023-05-10 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_food_food_des'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='food',
            name='food_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]