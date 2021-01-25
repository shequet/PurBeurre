from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ProductSearchForm
from .models import Product


def index(request):
    form = ProductSearchForm
    return render(request, 'home.html', {'form': form})


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
            products = Product.objects.filter(name__contains=name).order_by('nutri_score', )

            return render(request, 'product_search.html', {
                'search': request.POST.get('name', ''),
                'products': products,
            })
