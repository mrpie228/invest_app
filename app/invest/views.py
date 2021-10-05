from django.db.models import F, Sum
from django.shortcuts import render
from .parse_stocks import create_all, PATH_TO_STOCKS_DB_LIST
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from .models import *
from .serializers import *
import sqlite3
from django.http import Http404
import json
from itertools import groupby
from operator import attrgetter
from rest_framework.pagination import PageNumberPagination


class LoginAPIView(APIView):
    permission_class = permissions.IsAuthenticated


class LoginListView(generics.ListAPIView):
    permissions_classes = [permissions.IsAuthenticated, ]


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


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
            with open('dbs/ticker_and_desc.json') as file:
                tickers_with_desc = json.load(file)
                for asset in assets:
                    if asset[2] in tickers_with_desc:
                        desc = tickers_with_desc[asset[2]]

                    else:
                        desc = ''

                    with open(f'dbs/json_prices/{asset[2]}.json') as price_file:
                        price_json = json.load(price_file)
                        ks = list(price_json['Monthly Time Series'].keys())

                        values = []

                        for key in ks:
                            values.append(price_json['Monthly Time Series'][key]['2. high'])
                        price_json = [ks, values]
                        print(desc)
                        one_asset, created = Asset.objects.update_or_create(name=asset[1], ticker=asset[2],
                                                                            sector=asset[4],

                                                                            defaults={'price': asset[3],
                                                                                      'type': 'Stock',
                                                                                      'description': desc,
                                                                                      'price_json': price_json,
                                                                                      'icon': f'stocks_icon/{asset[2]}.svg'})
        conn.close()
        return Response(f'updated {len(assets)} stocks', status=status.HTTP_200_OK)


class AssetsView(generics.ListAPIView):
    serializer_class = AssetsSerializer
    pagination_class = PageNumberPagination
    queryset = assets = Asset.objects.all().order_by('name')


class AssetView(generics.RetrieveAPIView):
    def get(self, request, ticker):
        try:
            asset = Asset.objects.filter(ticker=ticker.upper()).first()
            serializer = AssetSerializer(asset)
        except:
            raise Http404("We cant find this asset")

        return Response(serializer.data)


class PortfolioView(LoginListView):
    def get(self, request):
        user = request.user
        items = Item.objects.filter(user=user).annotate(ticker=F('asset__ticker'), price=F('asset__price'))
        print(items)
        serializer = ItemSerializer(data=items, many=True)
        serializer.is_valid()
        assets = serializer.validated_data

        return Response(serializer.data, status=status.HTTP_200_OK)


class BuyAsset(LoginAPIView):
    serializer_class = BuyAssetSerializer

    def post(self, request):
        serializer = self.serializer_class(data={'ticker': request.data['ticker'], 'count': request.data['count']})
        serializer.is_valid()

        ticker = serializer.validated_data['ticker']
        count = serializer.validated_data['count']
        asset = Asset.objects.filter(ticker=ticker).first()

        def get_price(asset, count):
            return asset.price * count

        #
        item = Item.objects.filter(user=request.user, asset=asset).first()
        if item:
            item.count = item.count + float(count)
            item.purchase_price = item.purchase_price + asset.price
        else:
            item = Item.objects.create(user=request.user, asset=asset, count=count,
                                       purchase_price=get_price(asset, count))
        item.save()
        return Response('F', status=status.HTTP_200_OK)
