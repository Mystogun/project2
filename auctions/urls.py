from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Auth Routes
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # Listings Routes
    path("listings/<int:listing_id>/show", views.show_listing, name="show_listing"),
    path("listings/<int:listing_id>/bid", views.place_bid, name="place_bid"),
    path("listings/<int:listing_id>/close", views.close_bid, name="close_bid"),
    path("listings/<int:listing_id>/comment", views.store_comment, name="comment"),
    path("listings/create", views.create_listing, name="create_listing"),
    path("listings/store", views.store_listing, name="store_listing"),
    path("listings/watchlist", views.watchlist, name="watchlist"),
    path("listings/<int:listing_id>/watch", views.watch, name="watch"),
    path("listings/<int:listing_id>/unwatch", views.unwatch, name="unwatch"),

    # Categories Routes
    path("categories", views.list_categories, name="list_categories"),
    path("categories/<int:category_id>/show", views.show_category, name="show_category"),
]
