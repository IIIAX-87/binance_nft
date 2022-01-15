from django.urls import path
from bot import views

urlpatterns = [
    path('buyer/', views.BuyerView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
    path('transaction_top/', views.TopTransactions.as_view()),
    path('buyer_top/', views.TopBuyers.as_view()),
    path('product/', views.ProductView.as_view()),
    path('trade_type/', views.TradeTypeView.as_view()),
    path('nft_type/', views.NftTypeView.as_view()),
    path('currency/', views.CurrencyView.as_view()),
]
