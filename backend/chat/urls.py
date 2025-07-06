from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path

# 🔐 Auth JWT endpoints
from .views import ChatAPIView , ChatHistoryAPIView 

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    
    
    path('chat/', ChatAPIView.as_view(), name='chat'),    
    path('chat/history/', ChatHistoryAPIView.as_view(), name='chat_history'),


        
        
        
]
