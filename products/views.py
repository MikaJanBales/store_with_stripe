import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductLandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        product = Item.objects.get(name="book")
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'product': product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def buy(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Item.objects.get(id=product_id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
                'card',
            ],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })

# 'price_1M6yKKCFvr2ln9dx6ojPVwS6'
# redirect(checkout_session.url, code=303)
