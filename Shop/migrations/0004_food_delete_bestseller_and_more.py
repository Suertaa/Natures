# Generated by Django 4.2.1 on 2023-05-10 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(blank=True, max_length=50, null=True)),
                ('food_age', models.TextField(blank=True, max_length=50, null=True)),
                ('food_desc', models.TextField(blank=True, max_length=500, null=True)),
                ('food_review', models.TextField(blank=True, max_length=1000, null=True)),
                ('food_price', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('food_img', models.ImageField(upload_to='dogs/')),
                ('food_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Bestseller',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='contact_comment',
            new_name='contact_message',
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]