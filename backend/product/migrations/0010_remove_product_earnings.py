# Generated by Django 4.1.3 on 2022-12-09 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_earnings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='earnings',
        ),
    ]