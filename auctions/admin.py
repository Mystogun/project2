from django.contrib import admin

# Register your models here.
from auctions.models import Category, AuctionListing, Bid, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")


class AuctionListingAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "description", "status", "starting_bid", "imageUrl", "category_id", "creator_id", "created_at")


class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "value", "bidder_id", "listing_id", "created_at")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "listing_id", "user_id", "created_at")


admin.site.register(Category, CategoryAdmin)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)
