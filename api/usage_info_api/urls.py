from django.urls import path
from .views import UsageInfoView

urlpatterns = [
    path('',UsageInfoView.as_view(), name='info'),
]
