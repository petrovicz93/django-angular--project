# Generated by Django 2.1.3 on 2019-04-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
