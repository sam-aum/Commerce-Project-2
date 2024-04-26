# CS50W Project 2

## Commerce


            <!-- <div class="alert alert-danger" role="alert">
                {{ message }}
            </div> -->


                else:
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Bid failed",
            "updated": False
        })