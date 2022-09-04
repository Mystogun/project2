from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class AuctionListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True, blank=True)
    status = models.BooleanField()
    starting_bid = models.FloatField()
    imageUrl = models.URLField(null=True, blank=True)
    creator_id = models.ForeignKey('User', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Bid(models.Model):
    value = models.FloatField()
    listing_id = models.ForeignKey('AuctionListing', on_delete=models.CASCADE)
    bidder_id = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())


class Comment(models.Model):
    content = models.CharField(max_length=512)
    listing_id = models.ForeignKey('AuctionListing', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())


class WatchList(models.Model):
    listing_id = models.ForeignKey('AuctionListing', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)