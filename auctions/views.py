from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Category, AuctionListing, Bid, Comment, WatchList


def index(request):
    listings = AuctionListing.objects.filter(status=True)
    # listings = AuctionListing.objects.all()
    watchlist_count = len(WatchList.objects.filter(user_id=request.user.id))
    return render(request, "auctions/index.html",
                  {'page_title': 'Active Listings', 'listings': listings, 'watchlist_count': watchlist_count})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# ----------------listings----------------

def show_listing(request, listing_id):
    user_watchlist = WatchList.objects.filter(user_id=request.user.id)
    listing = AuctionListing.objects.get(id=listing_id)

    bids = Bid.objects.filter(listing_id=listing.id)

    min_bid = listing.starting_bid + 0.01
    max_bidder = None

    if len(bids) > 0:
        min_bid = max(bid.value for bid in bids)
        max_bidder = next(bid for bid in bids if bid.value == min_bid)
        min_bid += 0.01

    comments = Comment.objects.filter(listing_id=listing_id)

    should_show_close_button = request.user.username == listing.creator_id.username

    watchlist_count = len(user_watchlist)

    in_watchlist = False
    for item in user_watchlist:
        if item.listing_id.id == listing.id and item.user_id.id == request.user.id:
            in_watchlist = True

    return render(request, "auctions/listing_details.html",
                  {
                      "listing": listing,
                      "min_bid": min_bid,
                      "max_bidder": max_bidder,
                      "bids": bids,
                      "show_close_button": should_show_close_button,
                      "comments": comments,
                      'watchlist_count': watchlist_count,
                      'should_show_remove_watchlist': in_watchlist
                  })


def place_bid(request, listing_id):
    listing = AuctionListing.objects.get(id=listing_id)

    new_bid = Bid()
    new_bid.value = float(request.POST["new_bid"])
    new_bid.listing_id = listing
    new_bid.bidder_id = request.user
    new_bid.save()

    return redirect('show_listing', listing_id=listing.id)


def close_bid(request, listing_id):
    listing = AuctionListing.objects.get(id=listing_id)
    listing.status = False
    listing.save()
    return redirect('show_listing', listing_id=listing.id)


def store_comment(request, listing_id):
    listing = AuctionListing.objects.get(id=listing_id)

    new_comment = Comment()
    new_comment.content = request.POST['content']
    new_comment.listing_id = listing
    new_comment.user_id = request.user

    new_comment.save()
    return redirect("show_listing", listing_id=listing_id)


def create_listing(request):
    categories = Category.objects.all()
    watchlist_count = len(WatchList.objects.filter(user_id=request.user.id))
    return render(request, "auctions/listing_create.html",
                  {'categories': categories, 'watchlist_count': watchlist_count})


def store_listing(request):
    category = Category.objects.get(id=int(request.POST["category_id"]))

    new_listing = AuctionListing()
    new_listing.title = request.POST["title"]
    new_listing.starting_bid = int(request.POST["starting_bid"])
    new_listing.category_id = category
    new_listing.imageUrl = request.POST["image_url"]
    new_listing.description = request.POST["description"]
    new_listing.status = True
    new_listing.creator_id = request.user
    new_listing.save()

    return redirect('show_listing', listing_id=new_listing.id)


def watchlist(request):
    user_watchlist = WatchList.objects.filter(user_id=request.user.id)
    watchlist_count = len(WatchList.objects.filter(user_id=request.user.id))

    listings = []
    for item in user_watchlist:
        listings.append(item.listing_id)

    return render(request, "auctions/index.html",
                  {'page_title': f'{request.user.username} Watchlist', 'listings': listings,
                   'watchlist_count': watchlist_count})


def watch(request, listing_id):
    user_watchlist = WatchList()

    listing = AuctionListing.objects.get(id=listing_id)
    user_watchlist.listing_id = listing
    user_watchlist.user_id = request.user
    user_watchlist.save()

    return redirect('show_listing', listing_id=listing_id)


def unwatch(request, listing_id):
    WatchList.objects.get(listing_id=listing_id, user_id=request.user.id).delete()

    return redirect('show_listing', listing_id=listing_id)


# ----------------categories----------------
def list_categories(request):
    categories = Category.objects.all()
    watchlist_count = len(WatchList.objects.filter(user_id=request.user.id))
    return render(request, "auctions/category_index.html",
                  {"categories": categories, 'watchlist_count': watchlist_count})


def show_category(request, category_id):
    listings = AuctionListing.objects.filter(category_id=category_id)
    category_name = Category.objects.get(id=category_id)
    watchlist_count = len(WatchList.objects.filter(user_id=request.user.id))
    return render(request, "auctions/index.html", {'page_title': f'{category_name}: Listings', 'listings': listings,
                                                   'watchlist_count': watchlist_count})
