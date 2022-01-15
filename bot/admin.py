from django.contrib import admin
from bot.models import Transaction, TradeType, NftType, Buyer, Product, Currency
# Register your models here.

admin.site.register(Transaction)
admin.site.register(TradeType)
admin.site.register(NftType)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Currency)