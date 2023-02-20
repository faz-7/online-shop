from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart': cart})

    def post(self, request):
        cart = Cart(request)
        product_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        cart.update(product_id, quantity)
        return redirect('orders:cart')


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity'))
        cart.add(product, quantity)
        return redirect('products:landing')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('orders:cart')


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order.html', {'order': order})


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('orders:order_detail', order.id)
