# Generated by Django 4.1 on 2022-08-31 23:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auctionlisting_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 2, 30, 2, 15239)),
        ),
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 2, 30, 2, 15239)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 2, 30, 2, 15239)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 2, 30, 2, 15239)),
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlisting')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
