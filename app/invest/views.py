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


class LoginAPIView(APIView):
    permission_class = permissions.IsAuthenticated


class LoginListView(generics.ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]


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

    def get_queryset(self):
        try:
            assets = Asset.objects.all().order_by('name')
            serializer = AssetsSerializer(assets, many=True)
        except:
            raise Http404("We cant find this asset")

        return assets


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
        print(user)
        profile = Profile.objects.filter(user=user).first()
        portfolio = Portfolio.objects.filter(profile=profile).first()
        serializer = PortfolioSerializer(portfolio)

        return Response(serializer.data, status=status.HTTP_200_OK)
