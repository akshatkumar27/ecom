from typing import ItemsView
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products
from .models import Order
# Create your views here

def index(request):
# taking all product from database
    product_obj=Products.objects.all()
# search feature
    item_name=request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_obj=product_obj.filter(title__icontains=item_name)
# paginator code       
    paginator=Paginator(product_obj,4) 
    page=request.GET.get('page')
    product_obj=paginator.get_page(page)
    return render(request,'shop/index.html',{'product_obj':product_obj})

# detail of a particular Items
def detail(request,id):
    product_sobj=Products.objects.get(id=id)
    return render(request,'shop/details.html',{'product_sobj':product_sobj})


#  checkout view 
def checkout(request):
    if request.method=="POST":
        items=request.POST.get('items',"")
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        city=request.POST.get('city',"")
        state=request.POST.get('state',"")
       
        zipcode=request.POST.get('zipcode',"")
        total=request.POST.get('total',"")

        order=Order(items=items,name=name,email=email,address=address,state=state,city=city,zipcode=zipcode,total=total)    
        order.save()
    return render(request,'shop/checkout.html')