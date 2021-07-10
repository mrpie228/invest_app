from django.urls import path, include
from .views import *
from .endpoints import AssetOperation, ParseStocks, UpdateStocks

urlpatterns = [
    path('api/assets/', AssetsView.as_view()),
    path('api/asset/<ticker>', AssetView.as_view()),
    path('api/deal/', AssetOperation.as_view()),
    path('api/parse/stocks/', ParseStocks.as_view()),
    path('api/update/stocks/', UpdateStocks.as_view())
]
