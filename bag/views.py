from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ Aview to render the shopping-bag page """

    return render(request, "bag/bag.html")
