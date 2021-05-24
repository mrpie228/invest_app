from rest_framework import serializers
from .models import Asset, DealHistory, Portfolio


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['__all__', ]


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['__all__', ]


class DealHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DealHistory
        fields = ['__all__', ]
