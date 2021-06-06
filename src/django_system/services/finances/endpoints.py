from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from .serialisers import *
from django.conf import settings

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


def get_price(items):
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
