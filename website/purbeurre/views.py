from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from .forms import ProductSearchForm
from .models import Product, Category


def index(request):
    form = ProductSearchForm
    return render(request, 'home.html', {'form': form})


def legal_mentions(request):
    return render(request, 'legal_mentions.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def myfood(request):
    return render(request, 'myfood.html')


def product_detail(request, product_id):
    return render(request, 'product_detail.html', {
        'product': Product.objects.get(pk=product_id)
    })


def product_search(request):
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
