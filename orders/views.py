from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST' and len(cart) > 0:
        # create order
        order = Order.objects.create(user=request.user if request.user.is_authenticated else None)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_name=item['product'].name,
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return redirect('orders:checkout_success', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart': cart})


def checkout_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/checkout_success.html', {'order': order})
