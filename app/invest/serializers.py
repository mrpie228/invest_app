from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django import forms


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
    asset = AssetsInPortfolioSerializer()

    class Meta:
        model = Item
        fields = ['asset', 'count', 'purchase_price']


class BuyAssetSerializer(serializers.Serializer):
    ticker = serializers.CharField(max_length=256)
    count = serializers.DecimalField(max_digits=6, decimal_places=2)


class BuyAssetForm(forms.Form):
    ticker = forms.CharField(label='Label', max_length=100)
    count = forms.IntegerField(label='Count')
