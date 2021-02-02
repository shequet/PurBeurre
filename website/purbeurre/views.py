from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductSearchForm
from .models import Product, ProductSubstitute


def index(request):
    form = ProductSearchForm
    return render(request, 'home.html', {'form': form})


def legal_mentions(request):
    return render(request, 'legal_mentions.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def product_substitute(request):
    user = request.user
    substitute_products = ProductSubstitute.objects.filter(user=user)

    return render(request, 'product_substitute.html', {
        'substitute_products': substitute_products
    })


@login_required
def product_substitute_add(request, product_id, substitute_product_id):
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
    user = request.user
    ProductSubstitute.objects.filter(
        product_id=product_id,
        substitute_product_id=substitute_product_id,
        user=user
    ).delete()
    return redirect('product_substitute')


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
