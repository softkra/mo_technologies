# Generated by Django 4.0.6 on 2022-07-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0003_alter_logs_message_alter_logs_request_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='response_body',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='response body'),
        ),
    ]
