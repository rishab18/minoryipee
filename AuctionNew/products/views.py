from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import ProductUploadForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
import json
from .models import *
from .forms import ProductUploadForm, BidPostForm, SearchProductForm

# Create your views here.
#@require_http_methods(["GET", "POST"])
@require_POST
@login_required
def uploadProduct(request):
        print('hey')
        form = ProductUploadForm(request.POST, request.FILES)
        if (form.is_valid()):
            product = form.save(commit= False);
            print('hey')
            product.By = request.user
            product.save();
            return JsonResponse(data= {'id' : product.BidStart, 'name' : product.Title })
        else:
            return JsonResponse(status = 400, data = { 'errors' : dict(form.errors.items())})

@require_POST
@login_required
def postBid(request, id):
        form = BidPostForm(request.POST)
        if(form.is_valid()):
          bid = form.save(commit = False)
          bid.By = request.user
          ret = get_object_or_404(Product, id = id)
          bid.Item = ret.Title
          bid.save();
          return JsonResponse(data= {'id' : bid.BidPrice, 'by' : bid.By})
        else:
          return JsonResponse(status = 400, data = { 'errors' : dict(form.errors.items())})


@require_GET
@login_required
def product_list(request):
    products = Product.objects.all()
    context = { 'courses' : products }
    if request.user.is_superuser or request.user.is_admin:
      context['form'] = ProductUploadForm();
    return render(request, 'product/product_upload.html', context)


@login_required
@require_GET
def bid_list(request):
    products = Product.objects.all()
    context = { 'courses' : products }
    if request.user.is_superuser or request.user.is_admin:
      context['form'] = ProductUploadForm();
    return render(request, 'product/product_upload.html', context)


@require_GET
def search_product(request):
    name = request.GET.get('name')
    data = []
    if name:
        products = Product.objects.filter(Title__icontains == name)
        data = [{'id': item.id, 'title' : item.Title } for item in products ]
    return JsonResponse(data = { 'item' : data })

@require_GET
def category_search(request):
    category = request.GET.get('Category')
    data = []
    if category:
        products = Product.object.filter(Category_id = category)
    data = [{ 'id' : product.id, 'title' : product.Title} for product in products]
    return JsonResponse(data = { 'product' : data })

