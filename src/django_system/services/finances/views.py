from django.shortcuts import render
from .models import Asset, DealHistory, Portfolio
from rest_framework.response import Response
from django.http import Http404
from .serialisers import AssetSerializer, AssetsSerializer
from rest_framework import generics


class AssetView(generics.RetrieveAPIView):
    def get(self, request, ticker):
        try:
            asset = Asset.objects.get(ticker=ticker.upper())
            serializer = AssetSerializer(asset)
        except:
            raise Http404("We cant find this asset")

        return Response(serializer.data)


class AssetsView(generics.ListAPIView):
    serializer_class = AssetsSerializer

    def get_queryset(self):
        try:
            assets = Asset.objects.all()
            serializer = AssetsSerializer(assets, many=True)
        except:
            raise Http404("We cant find this asset")

        return assets


class PortfolioView(generics.RetrieveAPIView):
    def get(self, request, ticker):
        try:
            asset = Asset.objects.get(ticker=ticker, draft=False)
            serializer = AssetSerializer(asset)
        except:
            raise Http404("We cant find this asset")

        return Response(serializer.data)
