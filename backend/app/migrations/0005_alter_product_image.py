# Generated by Django 4.2.2 on 2023-06-06 18:56

import app.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                default="placeholder.png",
                null=True,
                upload_to=app.utils.upload_to,
            ),
        ),
    ]