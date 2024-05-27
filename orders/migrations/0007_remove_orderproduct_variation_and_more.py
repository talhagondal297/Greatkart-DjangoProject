# Generated by Django 5.0.6 on 2024-05-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_orderproduct_variation'),
        ('store', '0004_alter_reviewrating_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, null=True, to='store.variation'),
        ),
    ]
