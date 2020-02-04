# -*- coding:Utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from Cart.cart import Cart
from django.core.mail import send_mail
from django.urls import reverse_lazy


def order_create(request):
    cart = Cart(request)
    if len(cart) != 0:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()
                subject = "Rendelés no. {}".format(order.id).encode('utf-8')
                message = 'Kedves {}, \n\n'\
                          '{} azonosítójú rendelésed megkaptuk feldolgozás folyamatban!\n\n'\
                          'Üdvözlettel,\n'\
                          'Lufitorony'.format(order.last_name, order.id)
                message_from = ['lufitorony@gmail.com']
                message_to = ['{}'.format(order.email)]
                send_mail(subject, message, message_from, message_to)
                return render(request,
                              'orders/order_created.html',
                              {'order': order})
        else:
            form = OrderCreateForm()

        return render(request,
                      'orders/order_create.html',
                      {'cart': cart, 'form': form})
    else:
        request.session.flush()
        request.session.modified = True
        return render(request, 'home.html')


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/order_detail.html',
                  {'order': order})
