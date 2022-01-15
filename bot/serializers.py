from rest_framework import serializers
from bot.models import Transaction, Buyer, Product, NftType, Currency, TradeType


class TradeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeType
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class NftTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NftType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    nft_type = NftTypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_title', 'nft_type']


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)
    trade_type = TradeTypeSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'buyer', 'product', 'order_success_time', 'price', 'product_i', 'currency', 'trade_type']
