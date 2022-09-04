# Generated by Django 4.1 on 2022-08-27 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_auctionlisting_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 19, 20, 28, 269106)),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 19, 20, 28, 269106)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 19, 20, 28, 269106)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 19, 20, 28, 270106)),
        ),
    ]