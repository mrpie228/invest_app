from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import *
from django.conf import settings
from .parse_stocks import create_all, PATH_TO_STOCKS_DB_LIST
from .models import Asset
import sqlite3

# class AbsLoginRequiredAPIView(APIView, metaclass=abc.ABCMeta):
#     # permission_classes = (IsAuthenticated,)
#     pass
NORMAL_USER_COMMISSION = 10
PREMIUM_USER_COMMISSION = 5

OPERATION_TYPES = {'no_type': ' Без типа',
                   'buy_stock': 'Покупка акции/облигации',
                   'buy_crypto': 'Покупка токенизированных активов',
                   'sell_stock': 'Продажа акции/облигации',
                   'sell_crypto': 'Продажа токенизированных активов',
                   'exchange': 'Обмен'}


def     get_price(items):
    for item in items:
        assets_price = item.asset.price * items.count + assets_price
    return assets_price


def get_comission(user, assets_price):
    if user.user_role == 'user':
        comission = NORMAL_USER_COMMISSION + assets_price
    if user.user_role == 'premium':
        comission = PREMIUM_USER_COMMISSION + assets_price

    return comission


class AssetOperation(APIView):
    serializer_class = DealHistorySerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        operation_type = serializer.validated_data.get('deal_type')
        dealers = serializer.validated_data.get('dealers')
        deal_owner = serializer.validated_data.get('deal_owner')
        items = serializer.validated_data.get('items')

        if operation_type and dealers and dealers and items:
            price = get_price(items=items)
            comission = get_comission(user=request.user, assets_price=price)
            # NEED TO CREATE DEAL HISTORY
        return Response('context', status=status.HTTP_200_OK)


class ParseStocks(APIView):
    def get(self, request):
        try:
            count = create_all()
            response = Response(f'parsed {count} stocks', status=status.HTTP_200_OK)
        except Exception as e:
            response = Response('failed', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response


class UpdateStocks(APIView):
    def get(self, request):
        conn = sqlite3.connect(PATH_TO_STOCKS_DB_LIST)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM stocks_list")
            assets = cur.fetchall()

            for asset in assets:
                one_asset, created = Asset.objects.update_or_create(name=asset[1], ticker=asset[2], sector=asset[4],
                                                                    defaults={'price': asset[3], 'type': 'stock',
                                                                              'icon': f'stocks_icon/{asset[2]}.svg'})
        conn.close()
        return Response(f'updated {len(assets)} stocks', status=status.HTTP_200_OK)
