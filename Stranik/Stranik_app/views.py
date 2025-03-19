from django.shortcuts import render,  get_object_or_404, redirect
from .models import Rent
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
import json

def index(request):
    rents = Rent.objects.order_by('-date')[:4]
    
    rent_images = {
        rent.id: rent.images.filter(is_main=True).first()
        for rent in rents
    }

    context = {
        'rents': rents,
        'rent_images': rent_images,
    }

    return render(request, "index.html", context)

def user_login(request):
    return render(request, "login.html")

def user_signUp(request):
    return render(request, "signUp.html")

def aboutUs(request):
    return render(request, "./aboutUs.html")

def error(request):
    return render(request, "./404.html")

#----------------------------------------------------------rents sort def

def get_sorted_rents(category_name, sort_option, min_price=None, max_price=None):
    rents = Rent.objects.filter(category__name=category_name)

    if min_price is not None and max_price is not None:
        rents = rents.filter(cost_value__gte=min_price, cost_value__lte=max_price)

    if sort_option == "pop":
        rents = rents.order_by("-pop")
    elif sort_option == "price_asc":
        rents = rents.order_by("cost_value")
    elif sort_option == "price_desc":
        rents = rents.order_by("-cost_value")

    return rents

def servicesPageRent(request):
    sort_option = request.GET.get("sort", "pop") 
    min_price = request.GET.get("min_price") 
    max_price = request.GET.get("max_price")  

    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    rents = get_sorted_rents("Rent", sort_option, min_price, max_price) 
    

    items_per_page = 6
    paginator = Paginator(rents, items_per_page) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html = render_to_string("dinamic_sort/catalog_content.html", {"page_obj": page_obj})
        pagination_html = render_to_string("dinamic_sort/pagination.html", {"page_obj": page_obj})
        return JsonResponse({"html": html, "pagination": pagination_html})

    return render(request, "catalog/servicesPage.html", {
        "page_obj": page_obj,
        "category": "Rent",
        "sort_option": sort_option,
        "min_price": min_price,
        "max_price": max_price
    })


def servicesPageMovie(request):
    sort_option = request.GET.get("sort", "pop") 
    min_price = request.GET.get("min_price") 
    max_price = request.GET.get("max_price")  

    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    rents = get_sorted_rents("Movie", sort_option, min_price, max_price) 
    

    items_per_page = 6
    paginator = Paginator(rents, items_per_page) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html = render_to_string("dinamic_sort/catalog_content.html", {"page_obj": page_obj})
        pagination_html = render_to_string("dinamic_sort/pagination.html", {"page_obj": page_obj})
        return JsonResponse({"html": html, "pagination": pagination_html})

    return render(request, "catalog/servicesPage.html", {
        "page_obj": page_obj,
        "category": "Movie",
        "sort_option": sort_option,
        "min_price": min_price,
        "max_price": max_price
    })

def filter_rents(request):
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    rents = Rent.objects.all()

    if min_price is not None and max_price is not None:
        rents = rents.filter(cost_value__gte=min_price, cost_value__lte=max_price)

    html = render_to_string("dinamic_sort/catalog_content.html", {"page_obj": rents})

    return JsonResponse({"html": html})

#-------------------------------------------------------------------------------end rent site^   location bottom

def locationPageStreet(request):
    sort_option = request.GET.get("sort", "pop") 
    min_price = request.GET.get("min_price") 
    max_price = request.GET.get("max_price")  

    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    rents = get_sorted_rents("Street", sort_option, min_price, max_price) 

    items_per_page = 6
    paginator = Paginator(rents, items_per_page) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html = render_to_string("dinamic_sort/catalog_content.html", {"page_obj": page_obj})
        pagination_html = render_to_string("dinamic_sort/pagination.html", {"page_obj": page_obj})
        return JsonResponse({"html": html, "pagination": pagination_html})

    return render(request, "catalog/locationsPage.html", {
        "page_obj": page_obj,
        "category": "Street",
        "sort_option": sort_option,
        "min_price": min_price,
        "max_price": max_price
    })

def locationPageRoom(request):
    sort_option = request.GET.get("sort", "pop") 
    min_price = request.GET.get("min_price") 
    max_price = request.GET.get("max_price")  

    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    rents = get_sorted_rents("Room", sort_option, min_price, max_price) 

    items_per_page = 6
    paginator = Paginator(rents, items_per_page) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html = render_to_string("dinamic_sort/catalog_content.html", {"page_obj": page_obj})
        pagination_html = render_to_string("dinamic_sort/pagination.html", {"page_obj": page_obj})
        return JsonResponse({"html": html, "pagination": pagination_html})

    return render(request, "catalog/locationsPage.html", {
        "page_obj": page_obj,
        "category": "Room",
        "sort_option": sort_option,
        "min_price": min_price,
        "max_price": max_price
    })

def locationPageStudio(request):
    sort_option = request.GET.get("sort", "pop") 
    min_price = request.GET.get("min_price") 
    max_price = request.GET.get("max_price")  

    min_price = int(min_price) if min_price else None
    max_price = int(max_price) if max_price else None

    rents = get_sorted_rents("Studio", sort_option, min_price, max_price) 

    items_per_page = 6
    paginator = Paginator(rents, items_per_page) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html = render_to_string("dinamic_sort/catalog_content.html", {"page_obj": page_obj})
        pagination_html = render_to_string("dinamic_sort/pagination.html", {"page_obj": page_obj})
        return JsonResponse({"html": html, "pagination": pagination_html})

    return render(request, "catalog/locationsPage.html", {
        "page_obj": page_obj,
        "category": "Studio",
        "sort_option": sort_option,
        "min_price": min_price,
        "max_price": max_price
    })


#----------------------------------------------------------------- end location


def rent_detail(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    images = rent.images.all()
    main_image = images.filter(is_main=True).first() 
    additional_images = images.exclude(is_main=True)[:4] 

    rating = round(rent.pop, 1) 

    full_stars = int(rating) 
    half_star = 1 if rating - full_stars >= 0.5 else 0

    return render(request, "catalog/servicesDetailPage.html", {
        "rent": rent,
        "main_image": main_image,
        "additional_images": additional_images,
        "full_stars": range(full_stars),
        "half_star": half_star,
    })



#------------------------------------------------------------------- search

