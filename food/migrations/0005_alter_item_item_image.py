# Generated by Django 4.0.6 on 2022-12-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg', max_length=600),
        ),
    ]
