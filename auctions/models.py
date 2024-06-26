from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    price = models.FloatField()
    isActive = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    watchlist = models.ManyToManyField(User, related_name="listingWatchlist")

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.commenter} comment on {self.listing}"
    
class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidder")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingBid")
    bidPrice = models.FloatField()

    def __str__(self):
        return f"{self.bidPrice:.2f}"
    
