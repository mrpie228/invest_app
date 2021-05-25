from django.urls import path, include
from .views import *
urlpatterns = [
    path('assets/', AssetsView.as_view()),
    path('asset/<ticker>', AssetView.as_view()),
]
