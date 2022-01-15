from django.core.management.base import BaseCommand
import aiohttp
import asyncio

from bot.models import Transaction, Buyer, NftType, Currency, TradeType, Product


def get_tasks(session):
    tasks = []
    for i in range(1, 10):
        tasks.append(asyncio.create_task(session.get(f'https://www.binance.com/bapi/nft/v1/public/nft/homepage'
                                                     f'/announce?cursor={i}', ssl=False)))
    return tasks


async def get_responses(results):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            await asyncio.sleep(0.1)
            await response.text()
            results.append(await response.json())


def get_transactions(results):
    asyncio.get_event_loop().run_until_complete(get_responses(results))


def get_buyer(result):
    return Buyer.objects.get_or_create(buyer_name=result['buyerName'],
                                       defaults={'buyer_name': result['buyerName']}, )[0]


def get_nft_type(result):
    return NftType.objects.get_or_create(nft_type=int(result['nftType']),
                                         defaults={'nft_type': int(result['nftType'])}
                                         )[0]


def get_currency(result):
    return Currency.objects.get_or_create(name=result['currency'],
                                          defaults={'name': result['currency']}
                                          )[0]


def get_trade_type(result):
    return TradeType.objects.get_or_create(trade_type=result['tradeType'],
                                           defaults={'trade_type': result['tradeType']}
                                           )[0]


def get_product(result):
    return Product.objects.get_or_create(product_title=result['productTitle'],
                                         nft_type=get_nft_type(result),
                                         defaults={'product_title': result['productTitle'],
                                                   'nft_type': get_nft_type(result),
                                                   }, )[0]


def get_transaction(result):
    return Transaction.objects.get_or_create(product=get_product(result),
                                             buyer=get_buyer(result),
                                             order_success_time=result['orderSuccessTime'],
                                             price=result['price'],
                                             currency=get_currency(result),
                                             product_i=result['productId'],
                                             trade_type=get_trade_type(result),
                                             defaults={'buyer': get_buyer(result),
                                                       'product': get_product(result),
                                                       'order_success_time': result['orderSuccessTime'],
                                                       'price': result['price'],
                                                       'currency': get_currency(result),
                                                       'product_i': result['productId'],
                                                       'trade_type': get_trade_type(result),
                                                       }, )


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            results = []
            try:
                get_transactions(results=results)
                for result in results:
                    print(result['data']['orderSuccessAnnounces'][0])
                    get_transaction(result['data']['orderSuccessAnnounces'][0])
            except Exception as err:
                print(err)
