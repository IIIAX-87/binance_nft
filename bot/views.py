import json
import time

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
import django_filters.rest_framework
from bot.models import Product, TradeType, NftType, Currency, Transaction, Buyer
from bot.serializers import ProductSerializer, TradeTypeSerializer, NftTypeSerializer, CurrencySerializer, \
    TransactionSerializer, BuyerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class TradeTypeView(generics.ListAPIView):
    serializer_class = TradeTypeSerializer
    queryset = TradeType.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class NftTypeView(generics.ListAPIView):
    serializer_class = NftTypeSerializer
    queryset = NftType.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class CurrencyView(generics.ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class TransactionView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class BuyerView(generics.ListAPIView):
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'


class TopTransactions(APIView):
    def get(self, request):
        products = []
        for product in Product.objects.filter(nft_type=request.query_params['nft_type']):
            products.append({'id': product.id, 'product': product.product_title, 'count': len(Transaction.objects.filter(product=product))})
        queryset = sorted(products, key=lambda k: k['count'], reverse=True)
        return Response(queryset[:int(request.query_params['top'])])


class TopBuyers(APIView):
    def get(self, request):
        buyers = []
        for buyer in Buyer.objects.all():
            buyers.append({'id': buyer.id, 'buyer': buyer.buyer_name, 'count': len(Transaction.objects.filter(buyer=buyer))})
        queryset = sorted(buyers, key=lambda k: k['count'], reverse=True)
        return Response(queryset[:int(request.query_params['top'])])


class MyView(View):
    def get(self, request):
        product = request.GET.get("product")
        transactions = Transaction.objects.filter(product_id=product)
        print(time.time(), len(transactions))
        return JsonResponse({'ingredients': list(transactions)})
