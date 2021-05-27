from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serialisers import AssetSerializer, AssetsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from serialisers import *

# class AbsLoginRequiredAPIView(APIView, metaclass=abc.ABCMeta):
#     # permission_classes = (IsAuthenticated,)
#     pass
OPERATION_TYPES = {'no_type': ' Без типа',
                   'buy_stock': 'Покупка акции/облигации',
                   'buy_crypto': 'Покупка токенизированных активов',
                   'sell_stock': 'Продажа акции/облигации',
                   'sell_crypto': 'Продажа токенизированных активов',
                   'exchange': 'Обмен'}


# class AssetOperation(APIView):
#     serializer_class = DealHistorySerializer
#
#     def post(self, request, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         operation_type = serializer.validated_data.get('operation_type')
#
#         if operation_type in OPERATION_TYPES:
#             pass
#         # serializer = self.serializer_class(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#
#         return Response('context', status=status.HTTP_200_OK)
