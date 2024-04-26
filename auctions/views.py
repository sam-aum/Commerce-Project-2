from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import User, Category, Listing, Comment, Bid


def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    itemInList = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    try:
        currentBid = Bid.objects.get(listing=listingData)
    except Bid.DoesNotExist:
        currentBid = None

    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "itemInList": itemInList,
        "allComments": allComments,
        "currentBid": currentBid,
    })

def watchListDisplay(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

def removeWatchList(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))


def addWatchList(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    allCategories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": allCategories
    })

# display categories
# def displayCategories(request):
#     if request.method == "POST":
#         indexCategory = request.POST['category']
#         category = Category.objects.get(categoryName=indexCategory)
#         activeListings = Listing.objects.filter(isActive=True, category=category)
#         allCategories = Category.objects.all()
#         return render(request, "auctions/index.html", {
#             "listings": activeListings,
#             "categories": allCategories
#         })

#     return HttpResponseRedirect('/')

# display categories
def displayCategories(request, category_id):
    category = Category.objects.get(pk=category_id)
    activeListings = Listing.objects.filter(isActive=True, category=category)
    allCategories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": allCategories
    })


# Create Listings
def createListings(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories": allCategories
        })
    else:
        # Get data from the form
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        price = request.POST["price"]
        category = request.POST["category"]
        # get the user
        currentUser = request.user

        # Get all content on categories
        categoryData = Category.objects.get(categoryName=category)

        # create the listing
        newListing = Listing(
            title=title,
            description=description,
            image=image,
            price=float(price),
            category=categoryData,
            user=currentUser
        )

        # Insert the object into the database
        newListing.save()

        # Redirect to index page
        return HttpResponseRedirect(reverse("index"))


# Add Bid 
# def addBid(request, id):
#     makeBid = request.POST["bid"]
#     listingData = Listing.objects.get(pk=id)
#     currentUser = request.user
#     itemInList = request.user in listingData.watchlist.all()
#     allComments = Comment.objects.filter(listing=listingData)
#     try:
#         currentBid = Bid.objects.get(listing=listingData)
#     except Bid.DoesNotExist:
#         currentBid = None

#     if float(makeBid) > listingData.price:

#         newBid = Bid(
#             bidPrice=float(makeBid),
#             listing=listingData,
#             bidder=currentUser,
#         )

#         newBid.save()

#         return render(request, "auctions/listing.html", {
#             "listing": listingData,
#             "message": "Bid successful",
#             "updated": True,
#             "allComments": allComments,
#             "currentBid": currentBid,
#             "itemInList": itemInList,
#         })

def addBid(request, id):
    makeBid = float(request.POST["bid"])
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user

    if makeBid > listingData.price:
        newBid = Bid(
            bidPrice=makeBid,
            listing=listingData,
            bidder=currentUser,
        )
        newBid.save()
        messages.success(request, "Bid placed successfully.")

    else:
        messages.error(request, "Bid must be higher than the listing price. Bid not placed.")


    return redirect("listing", id=id)

# def addBid(request, id):
#     makeBid = request.POST["bid"]
#     listingData = Listing.objects.get(pk=id)
#     currentUser = request.user
    

#     newBid = Bid(
#         bidPrice=float(makeBid),
#         listing=listingData,
#         bidder=currentUser,
#     )

#     newBid.save()

#     return HttpResponseRedirect(reverse("listing", args=(id, )))


# Add Comment
def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    comment = request.POST["newComment"]

    newComment = Comment(
        commenter=currentUser,
        listing=listingData,
        comment=comment,
    )

    newComment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))

# User
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
