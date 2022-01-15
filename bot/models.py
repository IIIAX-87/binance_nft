from django.db import models

# Create your models here.


class TradeType(models.Model):
    trade_type = models.SmallIntegerField(blank=False)
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f'{str(self.trade_type)}'


class NftType(models.Model):
    nft_type = models.SmallIntegerField(blank=False)
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f'{str(self.nft_type)}'


class Product(models.Model):
    product_title = models.CharField(blank=False, max_length=250)
    nft_type = models.ForeignKey(NftType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.product_title)}: type - {self.nft_type}'


class Buyer(models.Model):
    buyer_name = models.CharField(blank=True, max_length=250)

    def __str__(self):
        return f'{str(self.buyer_name)}'


class Currency(models.Model):
    name = models.CharField(blank=True, max_length=15)

    def __str__(self):
        return f'{str(self.name)}'


class Transaction(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_success_time = models.BigIntegerField(blank=False)
    price = models.CharField(max_length=250, blank=False)
    product_i = models.BigIntegerField(blank=False)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    trade_type = models.ForeignKey(TradeType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.buyer)}: {self.product} (id {self.product_i}) - {self.price} {self.currency}, trade_type={self.trade_type}'

