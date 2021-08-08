from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # data processing
    path('parse/stocks/', ParseStocks.as_view()),
    path('update/stocks/', UpdateStocks.as_view()),

    # assets
    path('assets/', AssetsView.as_view(), name='assets_view'),
    path('asset/<ticker>', AssetView.as_view(), name='asset_view'),

    # portfolio
    path('portfolio/', PortfolioView.as_view(), name='portfolio_view')

]
