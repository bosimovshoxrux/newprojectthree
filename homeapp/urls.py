from django.urls import path
from .views import HomeappViews, MaruzalarViews, OyatlarViews, XadislarViews

urlpatterns = [
    path('', HomeappViews.as_view(), name='home'),
    path('', MaruzalarViews.as_view(), name='maruza'),
    path('', OyatlarViews.as_view(), name='maruza'),
    path('', XadislarViews.as_view(), name='maruza'),
]
