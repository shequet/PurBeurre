from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ProductSearchForm


def index(request):
    form = ProductSearchForm
    return render(request, 'home.html', {'form': form})


@login_required
def myfood(request):
    return render(request, 'myfood.html')


def product_detail(request, product_id):
    return render(request, 'product_detail.html', {
        'product': {
            'id': product_id,
            'name': 'Pizza surgelée',
            'description': 'blabla',
            'photo': 'https://static.openfoodfacts.org/images/products/327/016/071/7323/front_fr.27.200.jpg',
            'score': 'B'
        }
    })



def product_search(request):
    if request.method == "POST":
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            return render(request, 'product_search.html', {
                'search': request.POST.get('name', ''),
                'foods': [
                    {
                        'id': 1,
                        'name': 'Pizza surgelée',
                        'description': 'blabla',
                        'photo': 'https://static.openfoodfacts.org/images/products/327/016/071/7323/front_fr.27.200.jpg',
                        'score': 'B'
                    },
                    {
                        'id': 2,
                        'name': 'Pizza surgelée',
                        'description': 'blabla',
                        'photo': 'https://static.openfoodfacts.org/images/products/370/000/926/7813/front_fr.26.200.jpg',
                        'score': 'B'
                    },
                    {
                        'id': 3,
                        'name': 'Pizza surgelée',
                        'description': 'blabla',
                        'photo': 'https://static.openfoodfacts.org/images/products/327/016/071/7323/front_fr.27.200.jpg',
                        'score': 'B'
                    },
                    {
                        'id': 4,
                        'name': 'Pizza surgelée',
                        'description': 'blabla',
                        'photo': 'https://static.openfoodfacts.org/images/products/327/016/071/7323/front_fr.27.200.jpg',
                        'score': 'B'
                    }
                ]
            })
