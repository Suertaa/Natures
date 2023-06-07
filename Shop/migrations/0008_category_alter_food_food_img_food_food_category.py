# Generated by Django 4.2.1 on 2023-05-10 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_delete_contact_remove_food_food_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='food_img',
            field=models.ImageField(upload_to='food/'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.category'),
        ),
    ]
