# Generated by Django 4.0.4 on 2022-05-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_about_remove_delivery_icon_alter_delivery_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=False, verbose_name='access'),
        ),
    ]
