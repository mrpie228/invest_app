from rest_framework import serializers
from .models import Asset, DealHistory, Portfolio


class ApproverSearchSerializer(serializers.Serializer):
    search_text = serializers.CharField(required=False, allow_blank=True)


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['name', 'ticker', 'price', 'type', 'description']


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['icon', 'name', 'ticker', 'price', 'type']


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class DealHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DealHistory
        fields = '__all__'
