from django.urls import path, include
from .views import *
from .endpoints import AssetOperation, ParseStocks,UpdateStocks

urlpatterns = [
    path('assets/', AssetsView.as_view()),
    path('asset/<ticker>', AssetView.as_view()),
    path('deal/', AssetOperation.as_view()),
    path('parse/stocks/', ParseStocks.as_view()),
    path('update/stocks/', UpdateStocks.as_view())
]
