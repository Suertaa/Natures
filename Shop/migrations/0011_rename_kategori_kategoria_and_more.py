# Generated by Django 4.2.1 on 2023-05-11 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_adopt_delete_adoption'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kategori',
            new_name='Kategoria',
        ),
        migrations.RenameField(
            model_name='kategoria',
            old_name='kategori_id',
            new_name='kategoria_id',
        ),
        migrations.RenameField(
            model_name='kategoria',
            old_name='kategori_type',
            new_name='kategoria_type',
        ),
    ]