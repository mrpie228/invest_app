from django.urls import path, include
from .views import *
from .endpoints import AssetOperation

urlpatterns = [
    path('assets/', AssetsView.as_view()),
    path('asset/<ticker>', AssetView.as_view()),
    path('deal/', AssetOperation.as_view())
]
