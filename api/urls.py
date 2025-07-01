from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/token/pair/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', views.getRoutes, name='get-routes'),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
]
