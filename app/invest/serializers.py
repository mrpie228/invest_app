from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['icon', 'name', 'ticker', 'price', 'type', 'sector']


class AssetsInPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['icon', 'name', 'ticker', 'price', 'type', 'sector', 'price_json']


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['name', 'icon', 'ticker', 'price', 'sector', 'type', 'description', 'price_json']


class ItemSerializer(serializers.ModelSerializer):
    asset = AssetsInPortfolioSerializer(many=True)

    class Meta:
        model = Item
        fields = ['asset', 'count', 'purchase_price']


class PortfolioSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = ['items', 'sum']
