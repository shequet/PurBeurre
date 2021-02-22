"""
purbeurre app views document
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductSearchForm
from .models import Product, ProductSubstitute


def index(request):
    """
    Display the index of the site

    Returns:
        template : "home.html"
    """

    form = ProductSearchForm
    return render(request, 'home.html', {'form': form})


def legal_mentions(request):
    """
    Display the legal mentions of the site

    Returns:
        template : "legal_mentions.html"
    """

    return render(request, 'legal_mentions.html')


def contact(request):
    """
    Display the contact of the site

    Returns:
        template : "contact.html"
    """

    return render(request, 'contact.html')


@login_required
def product_substitute(request):
    """
    Display the product substitute of the site

    Returns:
        template : "product_substitute.html"
    """

    user = request.user
    substitute_products = ProductSubstitute.objects.filter(user=user)

    return render(request, 'product_substitute.html', {
        'substitute_products': substitute_products
    })


@login_required
def product_substitute_add(request, product_id, substitute_product_id):
    """
    Add the product substitute in database

    Returns:
        redirect : "product_substitute"
    """

    user = request.user
    ProductSubstitute.objects.get_or_create(
        product_id=product_id,
        substitute_product_id=substitute_product_id,
        user=user,
        defaults={
            'product_id': product_id,
            'substitute_product_id': substitute_product_id,
            'user': user
        },
    )
    return redirect('product_substitute')


@login_required
def product_substitute_delete(request, product_id, substitute_product_id):
    """
    Delete the product substitute in database

    Returns:
        redirect : "product_substitute"
    """

    user = request.user
    ProductSubstitute.objects.filter(
        product_id=product_id,
        substitute_product_id=substitute_product_id,
        user=user
    ).delete()
    return redirect('product_substitute')


def product_detail(request, product_id):
    """
    Display detail product

    Returns:
        template : "product_detail"
    """

    return render(request, 'product_detail.html', {
        'product': Product.objects.get(pk=product_id)
    })


def product_search(request):
    """
    Display the page for product search

    Returns:
        template : "product_search.html"
    """

    if request.method == "POST":
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            substitute_products = []
            product = Product.objects.filter(name__contains=name).first()

            if product is not None:
                substitute_products = Product.objects.filter(
                    category=product.category,
                    nutri_score__lt=product.nutri_score
                ).order_by('nutri_score', )[:50]

            return render(request, 'product_search.html', {
                'search': request.POST.get('name', ''),
                'product': product,
                'substitute_products': substitute_products,
            })
